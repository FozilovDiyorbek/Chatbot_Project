import gradio as gr
from nltk.chat.util import Chat, reflections

# Savol-javob juftliklari
pairs = (
    (
        r"salom (.*)",
        (
            "Salom! Qanday yordam bera olaman?",
            "Salom, qalaysiz? Sizga qanday yordam bera olaman?",
        ),
    ),

    (
        r"salom",
        (
            "Salom! Qanday yordam bera olaman?",
            "Salom, qalaysiz? Sizga qanday yordam bera olaman?",
        ),
    ),
    
    (
        r"isming (.*)",
        (
            "Mening ismim Eliza",
            "Men chatbotman, ismim Eliza",
        ),
    ),

    (
        r"(qandaysan|qalaysan|qalaysiz|yahshimisan|qalesan|tuzikmisan)(.*)",
        (
            "Rahmat, yaxshi! Siz-chi?",
            "Yaxshi, sizning kayfiyatingiz qalay?",
        ),
    ),  

    (
        r"(nima qilayapsan|nima qilyapsan)(.*)",
        (
            "Siz bilan suhbatlashyapman!",
            "Siz bilan gaplashyapman, siz-chi?",
        ),
    ),

    (
        r"(.*)(haqida malumot bera olasanmi|haqida aytib bera olasanmi|haqida nima bilasan|haqida malumot ber|bo'yicha malumot ber|to'g'risida nima nilasan)",
        (
            "%1 haqida sizga qanday ma'lumot kerak?",
            "Albatta, %1 haqida qanday savollaringiz bor?",
        ),
    ),

    (
        r"qaysi tilda gaplashasan",
        (
            "Men asosan o'zbek tilida gaplashaman, lekin boshqa tillarni ham tushunishim mumkin.",
        ),
    ),

    (
        r"(.*)(kim\?|kim)",
        (
            "%1 haqida ma'lumot olmoqchimisiz?",
            "Siz %1 haqida so'rayapsizmi? Batafsilroq yozing.",
        ),
    ),

    (
        r"(.*)(nima\?|nima)",
        (
            "%1 haqida ma'lumot beraymi?",
            "Siz %1 haqida so'rayapsizmi? Aniqroq yozing.",
        ),
    ),

    (
        r"(hozir soat nechchi\?|hozir soat nechchi|hozir so[gg']ot nechchi)",
        ("Men aniq vaqtni bilmayman, lekin qurilmangizdan tekshirib ko'ring!",),
    ),

    (
        r"(bugun qaysi kun\?|bugun qaysi kun|bugun qanday kun|bugun qanaqa kun|bugun nima kun)",
        ("Bugun haftaning qaysi kuni ekanini tekshirib ko'ring!",),
    ),

    (
        r"(ob-havo qanday\?|ob-havo qanday|bugun qanday ob havo|ob havo qanday)",
        ("Ob-havo haqida aniq ma'lumot bera olmayman, lekin telefoningizdan tekshirishingiz mumkin.",),
    ),

    (
        r"(yaxshi (.*) bilasanmi\?|yaxshi (.*) bilasanmi|yaxshi (.*) olasanmi)",
        (
            "Ehtimol, %1 haqida ayta olarman. Aniqroq so'rasangiz?",
            "Ha, %1 haqida ma'lumot bera olaman.",
        ),
    ),

    (
        r"(python haqida aytib bera olasanmi\?|python haqida aytib bera olasanmi|python nima)",
        (
            "Python - bu sodda va kuchli dasturlash tili. U sun'iy intellekt, veb-ishlab chiqish, ma'lumotlar tahlili va boshqa ko'plab sohalarda ishlatiladi.",
            "Python - ochiq kodli dasturlash tili bo'lib, uning sintaksisi oddiy va tushunarli.",
        ),
    ),

    (
        r"html nima\?",
        (
            "HTML - bu veb-sahifalarni yaratish uchun ishlatiladigan belgilar tilidir.",
            "HTML (HyperText Markup Language) veb-sahifalarning tuzilishini belgilash uchun ishlatiladi.",
        ),
    ),

    (
        r"css nima\?",
        (
            "CSS - bu veb-sahifalarni stilini belgilash uchun ishlatiladigan belgilar tilidir.",
            "CSS (Cascading Style Sheets) veb-sahifalarning stilini belgilash uchun ishlatiladi.",
        ),
    ),

    (
        r"(javascript nima\?|javascript nima)",
        (
            "JavaScript - bu veb-ishlab chiqishda keng qo'llaniladigan dasturlash tili.",
            "JavaScript veb-saytlarga interaktivlik qo'shish uchun ishlatiladi.",
        ),
    ),

    (
        r"(javascript haqida ma'lumot bera olasanmi\?|javascript haqida ma'lumot bera olasanmi|javascript haqida aytib ber|javascript haqida ma'lumot ber)",
        (
            "JavaScript - bu veb-ishlab chiqishda keng qo'llaniladigan dasturlash tili.",
            "JavaScript veb-saytlarga interaktivlik qo'shish uchun ishlatiladi.",
        ),
    ),

    (
        r"(m[ea]nga motivatsiya bera olasanmi\?|m[ea]nga motivatsiya bera olasanmi|m[ea]nga motivatsiya ber|m[ea]nga motivatsiya kerak)",
        (
            "Albatta! Hech qachon taslim bo'lmang, oldinga intiling! Harakat qilgan odam albatta muvaffaqiyatga erishadi!",
            "Siz juda zo'rsiz! Oldingizdagi qiyinchiliklarni yenga olasiz!",
        ),
    ),

    (
        r"(xayr|hayr|ko'rishguncha)",
        (
            "Xayr, yaxshi kun tilayman!",
            "Ko'rishguncha, salomat bo'ling!",
        ),
    ),

    (
        r"menga (.*) kerak",
        (
            "Sizga %1 kerak. Batafsilroq yozing.",
            "%1? Nimaga kerak? Aniqroq tushuntiring.",
        ),
    ),

    (
        r"(.*)",
        (
            "Aniqroq yozib ko'ringchi",
            "Savolni sal o'zgartirib beringchi",
            "To'liqroq ayting",
            "Nega bu savolni so'rayapsiz",
            "Qiziq",
            "O'ylab ko'rish kerak",
        ),
    ),
)

# Chatbot yaratish
chatbot = Chat(pairs, reflections)

# Gradio interfeysini yaratish
def chatbot_response(user_input):
    return chatbot.respond(user_input)

iface = gr.Interface(fn=chatbot_response, inputs="text", outputs="text", title="NLTK Chatbot")
iface.launch()