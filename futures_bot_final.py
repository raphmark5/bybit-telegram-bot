import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import ccxt

TELEGRAM_TOKEN = "7759175898:AAEMBxpN5ihvO9obOsA4O1tlUFk9OEzx6Vs"

exchange = ccxt.bybit({
    'enableRateLimit': True
})

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is online! Use /price to get BTC/USDT Futures price.")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        ticker = await exchange.fetch_ticker("BTC/USDT")
        price = ticker['last']
        await update.message.reply_text(f"📉 BTC/USDT Futures Price: ${price}")
    except Exception as e:
        await update.message.reply_text(f"❌ Failed to fetch price: {str(e)}")

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())