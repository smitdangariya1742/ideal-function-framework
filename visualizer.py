# visualizer.py
from bokeh.plotting import figure, output_file, save

def plot_mappings(training_df, ideal_df, selected, mapping_df, max_devs, output_path='output.html'):
    output_file(output_path)
    p = figure(title="Training and Ideal Functions", width=900, height=450)

    colors = ['navy', 'green', 'orange', 'purple']
    for i, col in enumerate(training_df.columns[1:]):
        p.line(training_df['X'], training_df[col], color=colors[i], legend_label=f'Train {i+1}', line_width=2)

    for idx in selected:
        col_name = f'Y{idx}'
        p.line(ideal_df['X'], ideal_df[col_name], line_dash='dashed', legend_label=f'Ideal {idx}')
        upper = ideal_df[col_name] + max_devs[idx]
        lower = ideal_df[col_name] - max_devs[idx]
        p.varea(x=ideal_df['X'], y1=lower, y2=upper, alpha=0.08)

    mapped = mapping_df.dropna(subset=['IdealFunc'])
    for idx in mapped['IdealFunc'].unique():
        df_sub = mapped[mapped['IdealFunc'] == idx]
        p.scatter(df_sub['X'], df_sub['Y'], size=6, marker='circle', legend_label=f'Mapped {int(idx)}')

    p.legend.click_policy = 'hide'
    save(p)
