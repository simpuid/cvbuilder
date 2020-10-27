from jinja2 import FileSystemLoader, Environment
import os

latex_jinja_env = Environment(
    block_start_string=r'\BLOCK{',
    block_end_string='}',
    variable_start_string=r'\VAR{',
    variable_end_string='}',
    comment_start_string=r'\#{',
    comment_end_string='}',
    line_statement_prefix='%% ',
    line_comment_prefix='%# ',
    trim_blocks=True,
    autoescape=False,
    loader=FileSystemLoader(os.path.abspath('.'))
)


def render_latex(uid: int):
    template = latex_jinja_env.get_template('generator/template.xtx')
    return template.render(id=uid)
