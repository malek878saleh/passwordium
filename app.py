import re
import math
import webbrowser
import customtkinter as ctk


# ==========================================
# PASSWORDIUM
# Developed by Malek F Saleh
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PasswordiumApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ------------------------------------------
        # WINDOW - 4:3 ASPECT RATIO
        # ------------------------------------------
        self.title("Passwordium - Advanced Password Analyzer")
        self.geometry("1000x750")
        self.resizable(False, False)

        # ------------------------------------------
        # COLORS
        # ------------------------------------------
        self.bg = "#030b1c"
        self.card = "#0a1730"
        self.input_bg = "#101d35"
        self.border = "#2d64ad"

        self.blue = "#1976e9"
        self.light_blue = "#5aaaff"

        self.text = "#dce5f3"
        self.muted = "#a9b6ca"

        self.configure(fg_color=self.bg)

        # ------------------------------------------
        # MAIN CONTAINER
        # ------------------------------------------
        main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        main.pack(
            fill="both",
            expand=True,
            padx=55,
            pady=(20, 0)
        )

        # ==========================================
        # HEADER
        # ==========================================

        header = ctk.CTkFrame(
            main,
            fg_color="transparent"
        )
        header.pack(pady=(0, 18))

        ctk.CTkLabel(
            header,
            text="🔐",
            font=("Arial", 38)
        ).pack(side="left", padx=(0, 12))

        title_area = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )
        title_area.pack(side="left")

        ctk.CTkLabel(
            title_area,
            text="PASSWORDIUM",
            font=("Arial", 32, "bold"),
            text_color="#76b5ff"
        ).pack(anchor="w")

        ctk.CTkLabel(
            title_area,
            text="Advanced Password Strength Analyzer",
            font=("Arial", 14),
            text_color=self.muted
        ).pack(anchor="w")

        # ==========================================
        # PASSWORD INPUT
        # ==========================================

        self.password_entry = ctk.CTkEntry(
            main,
            placeholder_text="Enter a password to analyze...",
            width=620,
            height=55,
            show="•",
            font=("Arial", 17),
            fg_color=self.input_bg,
            border_color="#3b70b7",
            border_width=1,
            corner_radius=14,
            text_color=self.text
        )
        self.password_entry.pack(pady=(0, 10))

        # Controls row
        controls = ctk.CTkFrame(
            main,
            fg_color="transparent"
        )
        controls.pack(
            fill="x",
            padx=10,
            pady=(0, 12)
        )

        self.show_password = ctk.CTkCheckBox(
            controls,
            text="Show password",
            font=("Arial", 14, "bold"),
            command=self.toggle_password,
            border_width=2
        )
        self.show_password.pack(side="left")

        ctk.CTkButton(
            controls,
            text="CLEAR  🗑",
            width=125,
            height=42,
            font=("Arial", 13, "bold"),
            fg_color="#101d35",
            border_width=1,
            border_color="#345d99",
            hover_color="#192b4a",
            command=self.clear_password
        ).pack(side="right")

        # Analyze button
        ctk.CTkButton(
            main,
            text="🔍   ANALYZE PASSWORD",
            width=300,
            height=52,
            font=("Arial", 16, "bold"),
            fg_color="#1768d8",
            hover_color="#1256b3",
            corner_radius=14,
            command=self.analyze
        ).pack(pady=(0, 15))

        # ==========================================
        # RESULTS CARD
        # ==========================================

        results_card = ctk.CTkFrame(
            main,
            fg_color=self.card,
            height=190,
            corner_radius=18,
            border_width=1,
            border_color="#3a659e"
        )
        results_card.pack(
            fill="x",
            pady=(0, 15)
        )

        self.result_label = ctk.CTkLabel(
            results_card,
            text="ENTER A PASSWORD",
            font=("Arial", 26, "bold"),
            text_color=self.text
        )
        self.result_label.pack(pady=(22, 15))

        self.progress_bar = ctk.CTkProgressBar(
            results_card,
            height=18,
            corner_radius=10,
            progress_color="#1988f5",
            fg_color="#39465a"
        )
        self.progress_bar.pack(
            fill="x",
            padx=50,
            pady=(0, 18)
        )
        self.progress_bar.set(0)

        # Stats
        stats = ctk.CTkFrame(
            results_card,
            fg_color="transparent"
        )
        stats.pack()

        # Score
        score_frame = ctk.CTkFrame(
            stats,
            fg_color="transparent"
        )
        score_frame.pack(
            side="left",
            padx=45
        )

        ctk.CTkLabel(
            score_frame,
            text="🛡  Security Score",
            font=("Arial", 14),
            text_color=self.text
        ).pack()

        self.score_label = ctk.CTkLabel(
            score_frame,
            text="-- / 100",
            font=("Arial", 21, "bold"),
            text_color=self.light_blue
        )
        self.score_label.pack()

        # Divider
        ctk.CTkFrame(
            stats,
            width=1,
            height=45,
            fg_color="#3c5578"
        ).pack(
            side="left",
            padx=20
        )

        # Entropy
        entropy_frame = ctk.CTkFrame(
            stats,
            fg_color="transparent"
        )
        entropy_frame.pack(
            side="left",
            padx=45
        )

        ctk.CTkLabel(
            entropy_frame,
            text="▥  Estimated Entropy",
            font=("Arial", 14),
            text_color=self.text
        ).pack()

        self.entropy_label = ctk.CTkLabel(
            entropy_frame,
            text="-- bits",
            font=("Arial", 21, "bold"),
            text_color=self.light_blue
        )
        self.entropy_label.pack()

        # ==========================================
        # SECURITY RECOMMENDATIONS
        # ==========================================

        recommendation_card = ctk.CTkFrame(
            main,
            fg_color=self.card,
            corner_radius=18,
            border_width=1,
            border_color="#1976d2"
        )
        recommendation_card.pack(
            fill="both",
            expand=True,
            pady=(0, 10)
        )

        ctk.CTkLabel(
            recommendation_card,
            text="💡  SECURITY RECOMMENDATIONS",
            font=("Arial", 16, "bold"),
            text_color="#56a7ff"
        ).pack(
            anchor="w",
            padx=22,
            pady=(15, 10)
        )

        self.feedback_box = ctk.CTkTextbox(
            recommendation_card,
            height=100,
            font=("Arial", 14),
            fg_color=self.input_bg,
            border_width=1,
            border_color="#29476f",
            corner_radius=12,
            text_color=self.text
        )
        self.feedback_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 18)
        )

        self.feedback_box.insert(
            "0.0",
            "🛡  Enter a password to receive a security analysis."
        )
        self.feedback_box.configure(state="disabled")

        # ==========================================
        # FOOTER
        # ==========================================

        footer = ctk.CTkFrame(
            self,
            height=60,
            fg_color="#061125",
            corner_radius=0,
            border_width=1,
            border_color="#183c69"
        )
        footer.pack(
            side="bottom",
            fill="x"
        )

        # Left
        left_footer = ctk.CTkFrame(
            footer,
            fg_color="transparent"
        )
        left_footer.pack(
            side="left",
            padx=20
        )

        ctk.CTkLabel(
            left_footer,
            text="</>",
            font=("Arial", 15, "bold"),
            text_color="#7aaeff"
        ).pack(side="left", padx=(0, 6))

        ctk.CTkLabel(
            left_footer,
            text="Developed by ",
            font=("Arial", 13),
            text_color=self.muted
        ).pack(side="left")

        ctk.CTkLabel(
            left_footer,
            text="Malek F Saleh",
            font=("Arial", 13, "bold"),
            text_color="#50a5ff"
        ).pack(side="left")

        # Center GitHub
        ctk.CTkButton(
            footer,
            text="◉  GitHub  ↗",
            width=165,
            height=42,
            font=("Arial", 14, "bold"),
            fg_color="#10213d",
            border_width=1,
            border_color="#168cff",
            hover_color="#17385f",
            corner_radius=21,
            command=self.open_github
        ).pack(
            side="left",
            expand=True
        )

        # Right
        ctk.CTkLabel(
            footer,
            text="🛡  Passwordium v1.0",
            font=("Arial", 13),
            text_color=self.muted
        ).pack(
            side="right",
            padx=20
        )

    # ==========================================
    # FUNCTIONS
    # ==========================================

    def open_github(self):
        webbrowser.open(
            "https://github.com/malek878saleh"
        )

    def toggle_password(self):
        if self.show_password.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="•")

    def clear_password(self):
        self.password_entry.delete(0, "end")
        self.analyze()

    def calculate_entropy(self, password):
        charset = 0

        if re.search(r"[a-z]", password):
            charset += 26

        if re.search(r"[A-Z]", password):
            charset += 26

        if re.search(r"\d", password):
            charset += 10

        if re.search(r"[^A-Za-z0-9]", password):
            charset += 32

        if charset == 0:
            return 0

        return len(password) * math.log2(charset)

    def analyze(self):
        password = self.password_entry.get()

        if not password:

            self.result_label.configure(
                text="ENTER A PASSWORD",
                text_color=self.text
            )

            self.score_label.configure(
                text="-- / 100",
                text_color=self.light_blue
            )

            self.entropy_label.configure(
                text="-- bits"
            )

            self.progress_bar.set(0)

            self.update_feedback(
                "🛡  Enter a password to receive a security analysis."
            )

            return

        score = 0
        feedback = []

        # Length
        if len(password) >= 16:
            score += 30
        elif len(password) >= 12:
            score += 25
        elif len(password) >= 8:
            score += 15
            feedback.append(
                "• Consider using at least 12 characters."
            )
        else:
            feedback.append(
                "• Password is too short. Use at least 12 characters."
            )

        # Lowercase
        if re.search(r"[a-z]", password):
            score += 15
        else:
            feedback.append(
                "• Add lowercase letters."
            )

        # Uppercase
        if re.search(r"[A-Z]", password):
            score += 15
        else:
            feedback.append(
                "• Add uppercase letters."
            )

        # Numbers
        if re.search(r"\d", password):
            score += 15
        else:
            feedback.append(
                "• Add numbers."
            )

        # Special characters
        if re.search(r"[^A-Za-z0-9]", password):
            score += 15
        else:
            feedback.append(
                "• Add special characters."
            )

        # Common passwords
        common = [
            "password",
            "123456",
            "qwerty",
            "admin",
            "letmein"
        ]

        for pattern in common:
            if pattern in password.lower():

                score -= 25

                feedback.append(
                    f"• Avoid common password pattern: {pattern}"
                )

        # Sequences
        if re.search(
            r"123|234|345|456|567|678|789",
            password
        ):
            score -= 10

            feedback.append(
                "• Avoid predictable number sequences."
            )

        score = max(0, min(100, score))

        # Strength
        if score >= 85:
            strength = "VERY STRONG"
            color = "#00d26a"

        elif score >= 65:
            strength = "STRONG"
            color = "#3da7ff"

        elif score >= 40:
            strength = "MEDIUM"
            color = "#ffb52b"

        else:
            strength = "WEAK"
            color = "#ff4d5e"

        entropy = self.calculate_entropy(password)

        self.result_label.configure(
            text=strength,
            text_color=color
        )

        self.score_label.configure(
            text=f"{score} / 100",
            text_color=color
        )

        self.entropy_label.configure(
            text=f"{entropy:.0f} bits",
            text_color=color
        )

        self.progress_bar.set(score / 100)

        self.progress_bar.configure(
            progress_color=color
        )

        if feedback:
            self.update_feedback(
                "\n".join(feedback)
            )
        else:
            self.update_feedback(
                "✓ Excellent! Your password passed all security checks."
            )

    def update_feedback(self, message):

        self.feedback_box.configure(
            state="normal"
        )

        self.feedback_box.delete(
            "0.0",
            "end"
        )

        self.feedback_box.insert(
            "0.0",
            message
        )

        self.feedback_box.configure(
            state="disabled"
        )


if __name__ == "__main__":
    app = PasswordiumApp()
    app.mainloop()