import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'JavaScript Projects'
chart.x_labels = ['vue', 'react', 'node']

plot_dicts = [
  {'value': 188066, 'label': ('🖖 Vue.js is a progressive, incrementally-'
    + 'adoptable JavaScript framework for building UI on the web.')},
  {'value': 174574, 'label': 'A declarative, efficient, and flexible '
    + 'JavaScript library for building user interfaces.'},
  {'value': 81711, 'label': 'Node.js JavaScript runtime :sparkles::'
    + 'turtle::rocket::sparkles:'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
