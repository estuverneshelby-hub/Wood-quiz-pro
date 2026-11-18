
import random

from kivy.app import App
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# =========================
# KONFIGIRASYON
# =========================

Window.clearcolor = (0.025, 0.04, 0.09, 1)

BLUE = (0.05, 0.28, 0.65, 1)
LIGHT_BLUE = (0.15, 0.55, 1, 1)
WHITE = (1, 1, 1, 1)
GOLD = (1, 0.78, 0.12, 1)
GREEN = (0.15, 0.85, 0.4, 1)
RED = (1, 0.25, 0.25, 1)

LEVELS = {
    1: "BEGINNER",
    2: "INTERMEDIATE",
    3: "EXPERT"
}

# =========================
# KESYON LEVEL 1
# =========================

questions = {
    1: {
        "KONESANS JENERAL": [
            {"question": "Konbyen jou yon semèn genyen?",
             "answers": ["5", "6", "7", "8"], "correct": 2},
            {"question": "Konbyen mwa yon ane genyen?",
             "answers": ["10", "11", "12", "13"], "correct": 2},
            {"question": "Ki bèt yo rele wa bèt yo?",
             "answers": ["Lyon", "Tig", "Chen", "Chat"], "correct": 0},
            {"question": "Konbyen èdtan yon jou genyen?",
             "answers": ["12", "18", "24", "30"], "correct": 2}
        ],

        "SYANS": [
            {"question": "Ki planèt nou rete?",
             "answers": ["Mas", "Latè", "Venis", "Jipitè"], "correct": 1},
            {"question": "Ki gaz moun bezwen pou respire?",
             "answers": ["Oksijèn", "Azòt", "Elyòm", "Idwojèn"], "correct": 0},
            {"question": "Ki ògàn ki ponpe san?",
             "answers": ["Poumon", "Kè", "Fwa", "Ren"], "correct": 1},
            {"question": "Ki pi gwo planèt nan sistèm solè a?",
             "answers": ["Latè", "Mas", "Jipitè", "Venis"], "correct": 2}
        ],

        "ISTWA": [
            {"question": "Nan ki ane Ayiti te vin endepandan?",
             "answers": ["1791", "1804", "1820", "1844"], "correct": 1},
            {"question": "Ki dat endepandans Ayiti?",
             "answers": ["1 Janvye", "18 Me", "20 Me", "14 Out"], "correct": 0},
            {"question": "Ki papa nasyon Ayisyen an?",
             "answers": ["Toussaint Louverture",
                         "Jean-Jacques Dessalines",
                         "Henri Christophe",
                         "Alexandre Pétion"], "correct": 1},
            {"question": "Ki revolisyon ki mennen Ayiti nan endepandans?",
             "answers": ["Revolisyon Endyen",
                         "Revolisyon Ayisyen",
                         "Revolisyon Franse",
                         "Revolisyon Ameriken"], "correct": 1}
        ],

        "JEWOGRAFI": [
            {"question": "Ki kapital peyi Ayiti?",
             "answers": ["Port-au-Prince", "Cap-Haïtien",
                         "Jacmel", "Les Cayes"], "correct": 0},
            {"question": "Konbyen depatman Ayiti genyen?",
             "answers": ["8", "10", "12", "14"], "correct": 1},
            {"question": "Ki pi gwo oseyan sou Latè?",
             "answers": ["Atlantik", "Pasifik", "Endyen", "Arktik"], "correct": 1},
            {"question": "Sou ki kontinan Ayiti ye?",
             "answers": ["Afrik", "Ewòp", "Amerik", "Azi"], "correct": 2}
        ],

        "ESPÒ": [
            {"question": "Konbyen jwè yon ekip foutbòl genyen sou teren an?",
             "answers": ["9", "10", "11", "12"], "correct": 2},
            {"question": "Ki espò yo jwe ak yon baskèt?",
             "answers": ["Foutbòl", "Basketball", "Tenis", "Natasyon"], "correct": 1},
            {"question": "Konbyen jwè basketball genyen sou teren an?",
             "answers": ["4", "5", "6", "7"], "correct": 1},
            {"question": "Nan ki peyi jwèt olenpik yo te kòmanse?",
             "answers": ["Grès", "Ayiti", "Kanada", "Brezil"], "correct": 0}
        ]
    }
}


# =========================
# KESYON LEVEL 2
# =========================

questions[2] = {
    "KONESANS JENERAL": [
        {"question": "Konbyen peyi ki gen manm nan Nasyonzini?",
         "answers": ["193", "150", "200", "175"], "correct": 0},
        {"question": "Ki lang ki pi pale nan Brezil?",
         "answers": ["Espanyòl", "Pòtigè", "Franse", "Anglè"], "correct": 1},
        {"question": "Ki syèk ane 2026 la fè pati?",
         "answers": ["19yèm", "20yèm", "21yèm", "22yèm"], "correct": 2},
        {"question": "Ki aparèy yo itilize pou mezire tanperati?",
         "answers": ["Baromèt", "Tèmomèt", "Voltmèt", "Altimèt"], "correct": 1}
    ],

    "SYANS": [
        {"question": "Ki senbòl chimik dlo?",
         "answers": ["CO2", "O2", "H2O", "NaCl"], "correct": 2},
        {"question": "Konbyen zo yon moun adilt genyen an jeneral?",
         "answers": ["106", "206", "306", "406"], "correct": 1},
        {"question": "Ki ògàn ki filtre san epi pwodui pipi?",
         "answers": ["Kè", "Ren", "Poumon", "Lestomak"], "correct": 1},
        {"question": "Ki fòs ki fè objè tonbe atè?",
         "answers": ["Mayetis", "Gravite", "Friksyon", "Presyon"], "correct": 1}
    ],

    "ISTWA": [
        {"question": "Nan ki ane Revolisyon Franse a te kòmanse?",
         "answers": ["1776", "1789", "1804", "1815"], "correct": 1},
        {"question": "Ki chèf ki te dirije lame endijèn nan nan batay Vertières?",
         "answers": ["Capois-la-Mort", "Pétion", "Christophe", "Toussaint"], "correct": 0},
        {"question": "Nan ki ane Toussaint Louverture te mouri?",
         "answers": ["1803", "1804", "1802", "1798"], "correct": 0},
        {"question": "Ki peyi ki te vann Louisiana bay Etazini an 1803?",
         "answers": ["Espay", "Lafrans", "Angletè", "Pòtigal"], "correct": 1}
    ],

    "JEWOGRAFI": [
        {"question": "Ki pi gwo peyi nan mond lan selon sipèfisi?",
         "answers": ["Kanada", "Lachin", "Larisi", "Etazini"], "correct": 2},
        {"question": "Ki kapital Japon?",
         "answers": ["Peken", "Seoul", "Tokyo", "Bangkok"], "correct": 2},
        {"question": "Ki dezè ki pi gwo dezè cho nan mond lan?",
         "answers": ["Gobi", "Sahara", "Kalahari", "Mojave"], "correct": 1},
        {"question": "Ki mòn ki pi wo sou Latè?",
         "answers": ["K2", "Kilimanjaro", "Everest", "Mont Blanc"], "correct": 2}
    ],

    "ESPÒ": [
        {"question": "Konbyen minit yon match foutbòl nòmal dire san tan adisyonèl?",
         "answers": ["80", "90", "100", "120"], "correct": 1},
        {"question": "Ki peyi ki te genyen Koup di Mond 2022?",
         "answers": ["Frans", "Brezil", "Ajantin", "Almay"], "correct": 2},
        {"question": "Nan ki espò yo itilize tèm 'love' pou zewo?",
         "answers": ["Basketball", "Tenis", "Boks", "Natasyon"], "correct": 1},
        {"question": "Konbyen bag senbòl olenpik la genyen?",
         "answers": ["4", "5", "6", "7"], "correct": 1}
    ]
}


# =========================
# KESYON LEVEL 3
# =========================

questions[3] = {
    "KONESANS JENERAL": [
        {"question": "Ki òganizasyon ki te fonde an 1945 pou ankouraje lapè entènasyonal?",
         "answers": ["NATO", "ONU", "OEA", "UNESCO"], "correct": 1},
        {"question": "Ki syantifik ki te devlope teyori relativite a?",
         "answers": ["Isaac Newton", "Albert Einstein", "Galileo", "Nikola Tesla"], "correct": 1},
        {"question": "Ki ane premye moun te mache sou Lalin?",
         "answers": ["1965", "1969", "1972", "1975"], "correct": 1},
        {"question": "Ki liv yo konsidere kòm premye gwo woman modèn nan?",
         "answers": ["Don Quixote", "Hamlet", "Iliad", "Odyssey"], "correct": 0}
    ],

    "SYANS": [
        {"question": "Ki eleman chimik ki gen senbòl Fe?",
         "answers": ["Fliyò", "Fè", "Fosfò", "Fermyòm"], "correct": 1},
        {"question": "Ki vitès limyè a nan vakyòm apeprè?",
         "answers": ["150 000 km/s", "300 000 km/s",
                     "500 000 km/s", "1 000 km/s"], "correct": 1},
        {"question": "Ki pati selil la ki pote enfòmasyon jenetik?",
         "answers": ["Manbràn", "ADN", "Sitoplas", "Ribozòm"], "correct": 1},
        {"question": "Ki non pwosesis plant yo itilize pou fè manje ak limyè?",
         "answers": ["Respirasyon", "Fotosentèz",
                     "Fermentasyon", "Evaporasyon"], "correct": 1}
    ],

    "ISTWA": [
        {"question": "Nan ki ane batay Vertières te fèt?",
         "answers": ["1791", "1802", "1803", "1804"], "correct": 2},
        {"question": "Ki dat batay Vertières te fèt?",
         "answers": ["18 Novanm 1803", "1 Janvye 1804",
                     "18 Me 1803", "14 Out 1791"], "correct": 0},
        {"question": "Ki chèf franse ki te voye ekspedisyon an Ayiti an 1802?",
         "answers": ["Napoleon Bonaparte",
                     "Charles X", "Louis XIV", "Robespierre"], "correct": 0},
        {"question": "Ki non premye chèf deta Ayiti apre endepandans?",
         "answers": ["Alexandre Pétion",
                     "Jean-Jacques Dessalines",
                     "Henri Christophe", "Toussaint Louverture"], "correct": 1}
    ],

    "JEWOGRAFI": [
        {"question": "Ki kanal ki separe Ewòp ak Afrik?",
         "answers": ["Kanal Panama", "Kanal La Manche",
                     "Dwat Gibraltar", "Kanal Suez"], "correct": 2},
        {"question": "Ki kapital Ostrali?",
         "answers": ["Sydney", "Melbourne", "Canberra", "Perth"], "correct": 2},
        {"question": "Ki rivyè ki gen pi gwo debi dlo nan mond lan?",
         "answers": ["Nil", "Amazon", "Mississippi", "Yangtze"], "correct": 1},
        {"question": "Ki peyi ki gen plis zile nan mond lan?",
         "answers": ["Filipin", "Endonezi", "Syèd", "Japon"], "correct": 2}
    ],

    "ESPÒ": [
        {"question": "Ki peyi ki te genyen premye Koup di Mond FIFA an 1930?",
         "answers": ["Brezil", "Ajantin", "Irigwe", "Itali"], "correct": 2},
        {"question": "Konbyen pwen yon tir twa pwen vo nan basketball?",
         "answers": ["1", "2", "3", "4"], "correct": 2},
        {"question": "Ki atlèt ki te genyen 8 meday lò nan Je Olenpik 2008?",
         "answers": ["Usain Bolt", "Michael Phelps",
                     "Carl Lewis", "Mark Spitz"], "correct": 1},
        {"question": "Konbyen Grand Slam tenis genyen nan yon ane?",
         "answers": ["2", "3", "4", "5"], "correct": 2}
    ]
}


# =========================
# BOUTON AK EKRAN JWE
# =========================

class QuizButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)
        self.color = WHITE
        self.bold = True
        self.font_size = "17sp"

        with self.canvas.before:
            self.bg_color = Color(*BLUE)
            self.bg_rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[18]
            )

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size


def make_label(text, size=20, color=WHITE, bold=False):
    return Label(
        text=str(text),
        font_size=f"{size}sp",
        color=color,
        bold=bold,
        halign="center",
        valign="middle"
    )


def make_spacer(height=10):
    return Widget(size_hint_y=None, height=height)


# =========================
# EKRAN AKÈY
# =========================

class HomeScreen(Screen):

    def on_enter(self):
        self.clear_widgets()

        app = App.get_running_app()

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        layout.add_widget(make_label(
            "WOOD QUIZ PRO",
            30, GOLD, True
        ))

        layout.add_widget(make_label(
            f"🪙 Pyès monnen: {app.total_coins}",
            19, GOLD, True
        ))

        layout.add_widget(make_label(
            f"🏆 Pi gwo nòt: {app.high_score}",
            18
        ))

        layout.add_widget(make_label(
            f"🔓 Nivo: {LEVELS[app.level]}",
            18, GREEN, True
        ))

        layout.add_widget(make_spacer(10))

        start = QuizButton(text="START QUIZ")
        start.size_hint_y = None
        start.height = 55
        start.bind(on_release=lambda x: setattr(
            self.manager, "current", "levels"
        ))
        layout.add_widget(start)

        exit_btn = QuizButton(text="EXIT")
        exit_btn.size_hint_y = None
        exit_btn.height = 50
        exit_btn.bind(on_release=lambda x: App.get_running_app().stop())
        layout.add_widget(exit_btn)

        self.add_widget(layout)


# =========================
# EKRAN NIVO
# =========================

class LevelScreen(Screen):

    def on_enter(self):
        self.clear_widgets()

        app = App.get_running_app()

        layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        layout.add_widget(make_label(
            "CHWAZI NIVO OU",
            25, GOLD, True
        ))

        for number, name in LEVELS.items():

            if number <= app.level:
                text = f"LEVEL {number} - {name} 🔓"
                color = GREEN
            else:
                text = f"LEVEL {number} - {name} 🔒"
                color = RED

            btn = QuizButton(text=text)
            btn.size_hint_y = None
            btn.height = 55
            btn.disabled = number > app.level

            btn.bind(
                on_release=lambda x, n=number:
                self.select_level(n)
            )

            layout.add_widget(btn)

        back = QuizButton(text="RETOUNEN")
        back.size_hint_y = None
        back.height = 45
        back.bind(on_release=lambda x: setattr(
            self.manager, "current", "home"
        ))

        layout.add_widget(back)
        self.add_widget(layout)

    def select_level(self, number):
        app = App.get_running_app()
        app.selected_level = number
        self.manager.current = "categories"


# =========================
# EKRAN KATEGORI
# =========================

class CategoryScreen(Screen):

    def on_enter(self):
        self.clear_widgets()

        app = App.get_running_app()

        layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        layout.add_widget(make_label(
            f"LEVEL {app.selected_level} - CHWAZI KATEGORI",
            21, GOLD, True
        ))

        for category in questions[app.selected_level].keys():

            btn = QuizButton(text=category)
            btn.size_hint_y = None
            btn.height = 48

            btn.bind(
                on_release=lambda x, c=category:
                self.select_category(c)
            )

            layout.add_widget(btn)

        back = QuizButton(text="RETOUNEN")
        back.size_hint_y = None
        back.height = 43
        back.bind(on_release=lambda x: setattr(
            self.manager, "current", "levels"
        ))

        layout.add_widget(back)
        self.add_widget(layout)

    def select_category(self, category):
        app = App.get_running_app()
        app.selected_category = category
        self.manager.current = "quiz"


# =========================
# EKRAN KESYON
# =========================

class QuizScreen(Screen):

    def on_enter(self):
        app = App.get_running_app()

        self.clear_widgets()

        self.selected_level = app.selected_level
        self.game_questions = list(
            questions[app.selected_level][app.selected_category]
        )

        random.shuffle(self.game_questions)

        self.index = 0
        self.score = 0
        self.time_left = 15
        self.answered = False
        self.previous_level = app.level

        self.layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=8
        )

        self.info = make_label("", 17, GOLD, True)
        self.layout.add_widget(self.info)

        self.timer_label = make_label("", 23, RED, True)
        self.layout.add_widget(self.timer_label)

        self.question_label = make_label("", 21, WHITE, True)
        self.layout.add_widget(self.question_label)

        self.answer_buttons = []

        for i in range(4):
            btn = QuizButton(text="")
            btn.size_hint_y = None
            btn.height = 48

            btn.bind(
                on_release=lambda x, n=i:
                self.check_answer(n)
            )

            self.answer_buttons.append(btn)
            self.layout.add_widget(btn)

        self.feedback = make_label("", 18, GREEN, True)
        self.layout.add_widget(self.feedback)

        self.add_widget(self.layout)

        self.show_question()

    def show_question(self):
        if self.index >= len(self.game_questions):
            self.finish_quiz()
            return

        self.answered = False
        self.time_left = 15

        question = self.game_questions[self.index]

        self.info.text = (
            f"Kesyon {self.index + 1}/4"
            f"     Nòt: {self.score}"
        )

        self.question_label.text = question["question"]
        self.feedback.text = ""

        for i, btn in enumerate(self.answer_buttons):
            btn.text = question["answers"][i]
            btn.disabled = False
            btn.bg_color.rgba = BLUE

        self.update_timer()
        Clock.unschedule(self.countdown)
        Clock.schedule_interval(self.countdown, 1)

    def update_timer(self):
        self.timer_label.text = f"⏳ {self.time_left} segonn"

    def countdown(self, dt):
        if self.answered:
            return False

        self.time_left -= 1
        self.update_timer()

        if self.time_left <= 0:
            self.timeout()
            return False

        return True

    def check_answer(self, choice):
        if self.answered:
            return

        self.answered = True
        Clock.unschedule(self.countdown)

        question = self.game_questions[self.index]

        for btn in self.answer_buttons:
            btn.disabled = True

        if choice == question["correct"]:
            self.score += 1
            self.feedback.text = "BON REPONS! +10 pyès 🪙"
            self.feedback.color = GREEN
            self.answer_buttons[choice].bg_color.rgba = GREEN
        else:
            self.feedback.text = "MOVE REPONS!"
            self.feedback.color = RED
            self.answer_buttons[choice].bg_color.rgba = RED
            self.answer_buttons[
                question["correct"]
            ].bg_color.rgba = GREEN

        Clock.schedule_once(self.next_question, 1.2)

    def timeout(self):
        if self.answered:
            return

        self.answered = True

        question = self.game_questions[self.index]

        for btn in self.answer_buttons:
            btn.disabled = True

        self.feedback.text = "TAN FINI! ⏰"
        self.feedback.color = RED

        self.answer_buttons[
            question["correct"]
        ].bg_color.rgba = GREEN

        Clock.schedule_once(self.next_question, 1.2)

    def next_question(self, dt):
        self.index += 1
        self.show_question()

    def finish_quiz(self):
        Clock.unschedule(self.countdown)

        app = App.get_running_app()

        app.total_coins += self.score * 10

        if self.score > app.high_score:
            app.high_score = self.score

        self.previous_level = app.level

        if self.selected_level == 1 and self.score >= 3:
            app.level = max(app.level, 2)

        elif self.selected_level == 2 and self.score == 4:
            app.level = max(app.level, 3)

        app.save_data()

        self.manager.current = "result"

    def on_leave(self):
        Clock.unschedule(self.countdown)


# =========================
# EKRAN REZILTA
# =========================

class ResultScreen(Screen):

    def on_enter(self):
        self.clear_widgets()

        app = App.get_running_app()
        quiz = self.manager.get_screen("quiz")

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        percentage = int((quiz.score / 4) * 100)

        layout.add_widget(make_label(
            "REZILTA JWE A",
            27, GOLD, True
        ))

        layout.add_widget(make_label(
            f"Nòt ou: {quiz.score}/4",
            25, GREEN, True
        ))

        layout.add_widget(make_label(
            f"Pousantaj: {percentage}%",
            20
        ))

        layout.add_widget(make_label(
            f"🪙 Ou genyen: +{quiz.score * 10} pyès",
            19, GOLD, True
        ))

        layout.add_widget(make_label(
            f"Total pyès: {app.total_coins}",
            18
        ))

        layout.add_widget(make_label(
            f"Pi gwo nòt: {app.high_score}",
            18
        ))

        if app.level > quiz.previous_level:
            layout.add_widget(make_label(
                f"🎉 LEVEL {app.level} DEBLOKE!",
                21, GREEN, True
            ))

        replay = QuizButton(text="CHWAZI YON LÒT NIVO")
        replay.size_hint_y = None
        replay.height = 50
        replay.bind(on_release=lambda x: setattr(
            self.manager, "current", "levels"
        ))
        layout.add_widget(replay)

        home = QuizButton(text="AKÈY")
        home.size_hint_y = None
        home.height = 48
        home.bind(on_release=lambda x: setattr(
            self.manager, "current", "home"
        ))
        layout.add_widget(home)

        self.add_widget(layout)


# =========================
# APLIKASYON PRINCIPAL
# =========================

class WoodQuizApp(App):

    def build(self):

        self.store = JsonStore("wood_quiz_data.json")

        self.total_coins = 0
        self.high_score = 0
        self.level = 1

        if self.store.exists("player"):
            data = self.store.get("player")

            self.total_coins = data.get("total_coins", 0)
            self.high_score = data.get("high_score", 0)
            self.level = data.get("level", 1)

        self.selected_level = 1
        self.selected_category = ""

        manager = ScreenManager()

        manager.add_widget(HomeScreen(name="home"))
        manager.add_widget(LevelScreen(name="levels"))
        manager.add_widget(CategoryScreen(name="categories"))
        manager.add_widget(QuizScreen(name="quiz"))
        manager.add_widget(ResultScreen(name="result"))

        manager.current = "home"

        return manager

    def save_data(self):
        self.store.put(
            "player",
            total_coins=self.total_coins,
            high_score=self.high_score,
            level=self.level
        )


if __name__ == "__main__":
    WoodQuizApp().run()
