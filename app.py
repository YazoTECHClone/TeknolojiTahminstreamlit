import streamlit as st
import matplotlib.pyplot as plt

# Başlık
st.title("Teknolojiye Ayırdığın Zaman Testi")
st.title("Merhaba Ben Yağız Gülbe  Bu siteyi ne kadar zamanımızı Teknolojiye ayırıyoruz onu grafik arıcılıyla gösterir ")
st.title("Kullandıklarım veri için #Pandas #matplotlib")

# Kullanıcıya sorular sormak
st.write("Bu test ile teknolojiye ayırdığın zamanı öğrenebilirsin.")

# Sorular ve cevaplar
questions = [
    "Oyun oynar mısın?",
    "İş yapar mısın?",
    "Sosyal medya kullanır mısın?",
    "YouTube'da video izler misin?",
    "Teknolojik haberleri takip eder misin?"
    "FPS Oyunları Oynarmısın"
    "Twiter Kullanırmısın"
    "Dualingo Kullanırmısnın"
]

# Cevapları tutmak için bir liste
answers = []

# Kullanıcıya her soru için radio butonları göster
for question in questions:
    answer = st.radio(question, options=["Hayır", "Evet"], key=question)
    answers.append(answer)

# Kullanıcı cevaplarını sayma (Evet = 1, Hayır = 0)
score = answers.count("Evet")

# Sonuçları gösterme
st.write(f"Test Sonucunuz: {score} / {len(questions)} soruya 'Evet' dediniz.")

# Zaman dilimi
time_spent = (score / len(questions)) * 100  # Yüzde olarak göster

# Grafik oluşturma
fig, ax = plt.subplots()
ax.barh(['Teknolojiye Ayırdığınız Zaman', 'Diğer Zaman'], [time_spent, 100 - time_spent], color=['green', 'gray'])
ax.set_xlabel('Zaman Yüzdesi')
ax.set_title('Teknolojiye Ayırdığınız Zaman')

# Grafik göster
st.pyplot(fig)

