from langdetect import detect

all_language_code ={
    "ar" : "Arab",
    "en" : "English",
    "de" : "German",
    "ru" : "Russian",
    "es" : "Spanish"
}

input_sentences =[
    "محمد بوترا نور اسماعيل ، واجب امتحان الفصل الدراسي النهائي لنظام دعم القرار",
    "Мухаммад Путра Нур Исмаил, Задание на заключительном семестре по системе поддержки принятия решений",
    "Muhamad Putra Nur Ismail, Decision Support System Semester Final Exam assignment",
    "Muhamad Putra Nur Ismail, Tarea del examen final del semestre del sistema de apoyo a la toma de decisiones"
    
]
lemmatizer_names = ['language Code','Input Sentence']
format_text = "{:24}" * (len(lemmatizer_names)+1)
print ("\n",format_text.format("Language Name", *lemmatizer_names),'\n','='*120)
for data in input_sentences:
    language_code = detect(data)
    sentence = [all_language_code.get(language_code), language_code, data]
    print(format_text.format(*sentence))
    

