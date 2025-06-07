import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

from utils import translate

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embedding = OpenAIEmbeddings()
vectorstore = FAISS.load_local("vectorstore", embedding)
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    retriever=vectorstore.as_retriever()
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ನಮಸ್ಕಾರ! ನಿಮ್ಮ ಪಾಠಪುಸ್ತಕದಿಂದ ಏನಾದರೂ ಕೇಳಿ 📘")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kn_query = update.message.text
    en_query = translate(kn_query, source="Kannada", target="English")
    en_answer = qa_chain.run(en_query)
    kn_answer = translate(en_answer, source="English", target="Kannada")
    await update.message.reply_text(kn_answer)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
