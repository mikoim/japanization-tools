import db
from jinja2 import Environment, FileSystemLoader


# http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader('template'))
    products = db.read_csv()

    # index
    index = env.get_template('index.tmpl')

    for page, prods in enumerate(chunks(products, 100)):
        with open('./output/index-{:d}.txt'.format(page), mode='w+', encoding='utf-8') as file:
            file.write(index.render(products=prods))

    # detail
    detail = env.get_template('detail.tmpl')

    for prod in products:
        with open('./output/detail-{:s}.txt'.format(prod['seq']), mode='w+', encoding='utf-8') as file:
            file.write(detail.render(product=prod))

    # curation
    curation = env.get_template('curation.tmpl')

    for prod in products:
        with open('./output/curation-{:s}.txt'.format(prod['seq']), mode='w+', encoding='utf-8') as file:
            file.write(curation.render(product=prod))
