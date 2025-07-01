# cryptowall

# 🛡️ CryptoWall 🛡️

[![GitHub stars](https://img.shields.io/github/stars/Mahdi6gh/cryptowall?style=social)](https://github.com/Mahdi6gh/cryptowall/stargazers)
[![Forks](https://img.shields.io/github/forks/Mahdi6gh/cryptowall?style=social)](https://github.com/Mahdi6gh/cryptowall/network/members)
[![Issues](https://img.shields.io/github/issues/Mahdi6gh/cryptowall)](https://github.com/Mahdi6gh/cryptowall/issues)

یک ابزار قدرتمند و ساده برای رمزنگاری و رمزگشایی فایل‌های شما با استفاده از الگوریتم‌های پیشرفته **AES** و **RSA**. با CryptoWall، امنیت داده‌های خود را تضمین کنید.

A powerful and simple tool for encrypting and decrypting your files using advanced **AES** and **RSA** algorithms. Ensure the security of your data with CryptoWall.

---

## 🌟 ویژگی‌ها (Features)

<div dir="rtl">

- **رمزنگاری ترکیبی:** استفاده همزمان از رمزنگاری متقارن (AES) برای سرعت بالا در رمزنگاری فایل‌ها و رمزنگاری نامتقارن (RSA) برای تبادل امن کلیدها.
- **امنیت بالا:** کلید AES که فایل‌ها با آن رمز می‌شوند، خود توسط کلید عمومی RSA رمزنگاری می‌شود. این یعنی فقط دارنده‌ی کلید خصوصی RSA قادر به رمزگشایی خواهد بود.
- **کاربری ساده:** فرآیند رمزنگاری و رمزگشایی به سادگی اجرای یک اسکریپت است.
- **پشتیبانی از پوشه‌ها:** امکان رمزنگاری تمام محتویات یک پوشه به صورت یکجا.

</div>

<br>

<div dir="ltr">

- **Hybrid Encryption:** Utilizes both symmetric encryption (AES) for high-speed file processing and asymmetric encryption (RSA) for secure key exchange.
- **High Security:** The AES key used to encrypt files is itself encrypted with an RSA public key. This means only the holder of the RSA private key can decrypt the data.
- **User-Friendly:** The encryption and decryption process is as simple as running a script.
- **Folder Support:** Capable of encrypting the entire contents of a specified folder at once.

</div>

---

## ⚙️ نحوه کارکرد (How It Works)

<p align="center">
  <img src="https://i.imgur.com/CHb9SoL.gif" alt="CryptoWall Animation" width="600"/>
</p>

1.  **تولید کلیدها (Key Generation):** ابتدا یک زوج کلید RSA (عمومی و خصوصی) ساخته می‌شود.
2.  **رمزنگاری فایل (File Encryption):**
    - یک کلید تصادفی AES برای هر فایل ساخته می‌شود.
    - فایل با استفاده از کلید AES رمزنگاری می‌شود.
    - کلید AES با استفاده از کلید عمومی RSA رمزنگاری می‌شود.
    - فایل رمز شده به همراه کلید AES رمز شده ذخیره می‌شوند.
3.  **رمزگشایی فایل (File Decryption):**
    - کلید خصوصی RSA، کلید رمز شده‌ی AES را رمزگشایی می‌کند.
    - با استفاده از کلید AES به دست آمده، فایل اصلی رمزگشایی می‌شود.

---

## 🚀 شروع سریع (Getting Started)

برای استفاده از این ابزار، مراحل زیر را دنبال کنید:

Follow these steps to use the tool:

### ۱. پیش‌نیازها (Prerequisites)

مطمئن شوید که پایتون و کتابخانه‌های مورد نیاز نصب هستند.

Make sure you have Python and the required libraries installed.

```bash
pip install pycryptodome
```

۲. کلون کردن پروژه (Cloning the Repository)

git clone [https://github.com/Mahdi6gh/cryptowall.git](https://github.com/Mahdi6gh/cryptowall.git)
cd cryptowall

python main.py

پس از اجرای موفقیت‌آمیز، کلیدهای private_key.pem و public_key.pem به همراه پوشه رمزنگاری شده شما ایجاد خواهند شد. کلید خصوصی خود (private_key.pem) را در مکانی امن نگهداری کنید!

After successful execution, the private_key.pem and public_key.pem keys will be generated along with your encrypted folder. Keep your private key (private_key.pem) in a secure place!

🤝 مشارکت (Contributing)
از مشارکت شما در این پروژه استقبال می‌کنیم. برای ارائه پیشنهادات یا گزارش خطاها، لطفاً یک Issue جدید ثبت کنید یا یک Pull Request ارسال نمایید.

Contributions are welcome! For suggestions or bug reports, please open an Issue or submit a Pull Request.
