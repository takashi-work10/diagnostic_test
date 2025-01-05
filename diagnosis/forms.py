# diagnosis/forms.py
from django import forms

class MBTIForm(forms.Form):
    """
    20個の質問を動的にセットする。
    各質問の回答は -3 ～ +3 (文字列) をHTML側でラジオボタンとして指定し、
    ここでは CharField として受け取る。
    """
    QUESTIONS = [
        "Q1. 朝起きると不安になることが多い",
        "Q2. 人前で意見を言う場面は苦手",
        "Q3. 少しの失敗でも強く落ち込む",
        "Q4. 些細な体調変化が気になる",
        "Q5. 他人からの評価を気にしやすい",
        "Q6. 将来に漠然とした不安を感じる",
        "Q7. 完璧にやらないと気が済まない",
        "Q8. 大勢の集まりより一人の時間を好む",
        "Q9. 予期しない変化にストレスを感じる",
        "Q10. 締め切りが近づくと強い焦りを感じる",
        "Q11. 周囲の雑音で集中できない",
        "Q12. 少しのことで責められるのが怖い",
        "Q13. ネガティブ思考に陥りやすい",
        "Q14. あれこれと深く考えすぎる",
        "Q15. 身体症状があると重大な病気を疑う",
        "Q16. 何もやる気が起きない時がある",
        "Q17. 批判を聞くと落ち込みが長引く",
        "Q18. 仕事や勉強が手につかなくなることがある",
        "Q19. 些細なことで動揺しやすい",
        "Q20. この先どうなるかと不安になることが多い",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 20個ぶんフィールドを動的に追加
        for i, text in enumerate(self.QUESTIONS, start=1):
            field_name = f"q{i}"
            self.fields[field_name] = forms.CharField(
                label=text,
                required=False,
            )
