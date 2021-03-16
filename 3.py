f = lambda A, n=3: [A[i:i + n] for i in range(0, len(A), n)]


def appearance(times):
    f = lambda A, n=2: [A[i:i + n] for i in range(0, len(A), n)]
    times['pupil']= f(times['pupil'])
    times['tutor'] = f(times['tutor'])
    print(times)


print(appearance({
    'lesson': [3200, 6800],
    'pupil': [3340, 3389, 3390, 3395, 3396, 6472],
    'tutor': [3290, 3430, 3443, 6473]
}))
