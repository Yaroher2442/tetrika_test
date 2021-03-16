from flask import Flask, request, jsonify

app = Flask(__name__)


def appearance(times):
    f = lambda A, n=2: [A[i:i + n] for i in range(0, len(A), n)]
    pupil = f(times['pupil'])
    tutor = f(times['tutor'])
    ls_p = []
    for i in pupil:
        ls_p += [j for j in range(min(i), max(i))]
    ls_t = []
    for i in tutor:
        ls_t += [j for j in range(min(i), max(i))]

    all_time_min = [min(times['pupil'])] + [min(times['tutor'])]
    all_time_max = [max(times['pupil'])] + [max(times['tutor'])]
    print(all_time_min, all_time_max)
    raz = []
    raz.append(max(all_time_min))
    intersect = list(set(ls_p).intersection(set(ls_t)))
    for i in range(0, len(intersect)):
        if intersect[i] - intersect[i - 1] > 1:
            print(True, intersect[i - 1], intersect[i])
            raz.append(intersect[i - 1])
            raz.append(intersect[i])
    raz.append(min(all_time_max))
    return sum([i[1] - i[0] for i in f(raz)])


@app.route("/get_appearance", methods=['POST'])
def hello():
    if request.json:
        content = request.json
        try:
            a, b, c = content['lesson'], content['pupil'], content['tutor']
            return jsonify({'appearance': appearance(content)})
        except:
            return jsonify({'error':'content not allowed'})
    else:
        return jsonify({'error':'content not allowed'})


if __name__ == "__main__":
    app.run(debug=True)
