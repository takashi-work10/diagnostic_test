# diagnosis/forms.py
from django import forms

class DiagnosisForm(forms.Form):
    """
    20個の質問をChoiceField(1~5)で受け取り
    labelに実際の質問文を記載
    """
    CHOICES = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]

    q1  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q1. 「先々のこと」を考えて、根拠のない不安や焦りに襲われることが多い")
    q2  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q2. 人前で意見を言う場面を想像するだけで、体がこわばる")
    q3  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q3. 「もし〇〇だとしたら？」と悪い方へ想像しすぎて、気づくと落ち込んでいる")
    q4  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q4. 対人関係で、相手のちょっとした言い方に必要以上にショックを受ける")
    q5  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q5. 誰かから否定的なコメントをされると、長時間引きずってしまう")
    q6  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q6. 物事を 100% 完璧にしないと気が済まないが、実際には疲れ果てる")
    q7  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q7. 些細な体調変化でも「大きな病気かも…」と不安になる")
    q8  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q8. 未来や人生の意味を考えると、急に怖さやむなしさを感じる")
    q9  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q9. 過去の痛い経験を思い出して、心拍数が上がったり涙が出たりして止まらない")
    q10 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q10. 仕事や勉強など、常に時間に追われている気がして気が休まらない")
    q11 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q11. 「将来この状況がもっと悪くなるかも…」とネガティブ連想しがち")
    q12 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q12. 何気ない会話でも、相手に「嫌われたかも」「不機嫌かも」と過剰に推測してしまう")
    q13 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q13. 少しでも失敗や不完全さを感じると「自分はダメだ」と強く思い込む")
    q14 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q14. 「健康診断で問題なし」と言われても「検査漏れかも…」と気になってしまう")
    q15 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q15. 夜、突然「死ぬってどうなるの？」と不安が止まらなくなる")
    q16 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q16. 似たシチュエーションを見るだけで、痛い過去がリアルに蘇って苦しくなる")
    q17 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q17. 周囲が忙しく動いていると、自分も何かしなきゃと強烈に焦る")
    q18 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q18. 「人が注目している」と意識した瞬間に、うまく話せなくなることが多い")
    q19 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q19. 失敗やミスを責められるのが怖くて、行動する前からドキドキが止まらない")
    q20 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Q20. 休みの日でも「本当に休んでいていいのか…」と不安になり休めない")

