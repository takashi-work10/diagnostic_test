# diagnosis/views.py
from django.shortcuts import render
from .forms import DiagnosisForm
from .models import DiagnosisResult

def index_view(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            # (1) 回答をリスト化
            answers = []
            for i in range(1, 21):
                val_str = form.cleaned_data[f'q{i}']  # ex: "1" ~ "5"
                answers.append(int(val_str))

            # (2) スコア計算
            future_score = answers[0] + answers[2] + answers[10]
            social_score = answers[1] + answers[3] + answers[11] + answers[17]
            evaluation_score = answers[4] + answers[18]
            perfection_score = answers[5] + answers[12]
            health_score = answers[6] + answers[13]
            existential_score = answers[7] + answers[14]
            trauma_score = answers[8] + answers[15]
            pressure_score = answers[9] + answers[16] + answers[19]
            scores = {
                '未来予報ビクビク型': future_score,
                '人間関係オロオロ型': social_score,
                '評価ドキドキ型': evaluation_score,
                '完璧主義パニック型': perfection_score,
                '健康オタオタ型': health_score,
                '存在意義グラグラ型': existential_score,
                'トラウマシンドローム型': trauma_score,
                'プレッシャー爆発型': pressure_score
            }
            best_type = max(scores, key=scores.get)

            # (3) DBに保存
            #    models.pyで定義したDiagnosisResultに答えを格納
            #    ここでは question1～question20 全部に書き込む
            result_obj = DiagnosisResult.objects.create(
                question1=answers[0],
                question2=answers[1],
                question3=answers[2],
                question4=answers[3],
                question5=answers[4],
                question6=answers[5],
                question7=answers[6],
                question8=answers[7],
                question9=answers[8],
                question10=answers[9],
                question11=answers[10],
                question12=answers[11],
                question13=answers[12],
                question14=answers[13],
                question15=answers[14],
                question16=answers[15],
                question17=answers[16],
                question18=answers[17],
                question19=answers[18],
                question20=answers[19],
            )

            # (4) 結果画面へ
            return render(request, 'diagnosis/result.html', {
                'best_type': best_type,
                'scores': scores,
            })
    else:
        form = DiagnosisForm()

    return render(request, 'diagnosis/index.html', {'form': form})
