import argparse


def format_text_block(frame_height, frame_width, file_name):
    answ = ''
    with open(file_name) as f:
        answ += f.readline().rstrip()[:frame_width]
        answ += '\n'


parser = argparse.ArgumentParser(description='Calculate Profit and Loss (P&L)')
parser.add_argument('--frame-height', type=int)
parser.add_argument('--frame-width', type=int)

args = parser.parse_args()

answ = 0
match args.get_by:
    case 'day':
        try:
            answ += args.per_day
        except Exception:
            pass
        try:
            answ += args.per_year / 360
        except Exception:
            pass
        try:
            answ += args.per_week / 7
        except Exception:
            pass
        try:
            answ += args.per_month / 30
        except Exception:
            pass
    case 'month':
        try:
            answ += args.per_month
        except Exception:
            pass
        try:
            answ += args.per_year / 12
        except Exception:
            pass
        try:
            answ += args.per_day * 30
        except Exception:
            pass
        try:
            answ += (args.per_week / 7) * 30
        except Exception:
            pass
    case 'year':
        try:
            answ += args.per_year
        except Exception:
            pass
        try:
            answ += args.per_month / 30 * 360
        except Exception:
            pass
        try:
            answ += args.per_day * 360
        except Exception:
            pass
        try:
            answ += (args.per_week / 7) * 360
        except Exception:
            pass
print(int(answ))
