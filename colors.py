import seaborn as sns

NESTS = ['E1', 'E2', 'E3', 'E4', 'E5', 'U1', 'U2', 'U3', 'U4', 'U5']
POSTNATALDAYS = [1, 2, 4, 5, 9, 10]
MOTHERS = ['E', 'U']

POSTNATALDAYPALETTE = sns.husl_palette(n_colors=len(POSTNATALDAYS), h=0.01, s=0.9, l=0.65)
NESTPALETTE = sns.color_palette("bright", n_colors=len(NESTS), desat=1)

COLORS = {
    'vocalization': {
        1: 'tab:blue',
        2: 'tab:orange'
    },
    'postnatalday': dict(zip(POSTNATALDAYS, POSTNATALDAYPALETTE)),
    'nest': dict(zip(NESTS, NESTPALETTE)),
    'mother': {
        'E': '#FFFF00',  # yellow
        'U': '#FF8C00'  # orange
    },
    'year':{
        17: "purple",
        19: 'green'
    }
}

sns.palplot(POSTNATALDAYPALETTE)
sns.palplot(NESTPALETTE)