# diagnosis/views.py
from django.shortcuts import render
from .forms import MBTIForm
from .models import DiagnosisResult

def index(request):
    if request.method == 'POST':
        form = MBTIForm(request.POST)
        if form.is_valid():
            # 20個分の回答取得
            answers_int = []
            for i in range(1, 21):
                field_name = f"q{i}"
                val_str = form.cleaned_data.get(field_name)
                if val_str:
                    answers_int.append(int(val_str))
                else:
                    answers_int.append(0)

            total_score = sum(answers_int)
            # 8パターンに分ける
            result_type = get_anxiety_type(total_score)

            # DB保存: DiagnosisAnswer オブジェクト作成
            diagnosis_obj = DiagnosisResult.objects.create(
                q1 = answers_int[0],
                q2 = answers_int[1],
                q3 = answers_int[2],
                q4 = answers_int[3],
                q5 = answers_int[4],
                q6 = answers_int[5],
                q7 = answers_int[6],
                q8 = answers_int[7],
                q9 = answers_int[8],
                q10 = answers_int[9],
                q11 = answers_int[10],
                q12 = answers_int[11],
                q13 = answers_int[12],
                q14 = answers_int[13],
                q15 = answers_int[14],
                q16 = answers_int[15],
                q17 = answers_int[16],
                q18 = answers_int[17],
                q19 = answers_int[18],
                q20 = answers_int[19],
                result_type = result_type
            )

            context = {
                'total_score': total_score,
                'result_type': result_type,
            }
            return render(request, 'diagnosis/result.html', context)

    else:
        form = MBTIForm()

    return render(request, 'diagnosis/index.html', {'form': form})


def get_anxiety_type(score):
    """
    合計スコア(-60 ~ +60)を8つに振り分ける例
    ※実際の質問やロジックに合わせて範囲を変えてください
    """
    if score <= -46:
        return "未来予報ビクビク型（将来不安）"
    elif score <= -31:
        return "人間関係オロオロ型（対人不安）"
    elif score <= -16:
        return "評価ドキドキ型（評価不安）"
    elif score <= -1:
        return "完璧主義パニック型（完璧主義）"
    elif score <= 14:
        return "健康オタオタ型（健康不安）"
    elif score <= 29:
        return "存在意義グラグラ型（存在論的不安）"
    elif score <= 44:
        return "トラウマシンドローム型（トラウマ起因）"
    else:
        return "プレッシャー爆発型（高ストレス環境）"
