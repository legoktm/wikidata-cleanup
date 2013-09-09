#!/data/project/legobot/python/bin/python

# Public domain
# By Legoktm

from wmflabs import db
import os


query = """
select
term_entity_id,
term_text
from wb_terms
where term_entity_type="item"
and term_language="en"
and term_type="description"
and term_text like "%."
limit 1000;
"""

def make_link(_id):
    return '<a href="https://www.wikidata.org/wiki/Q{0}">Q{0}</a>'.format(_id)

with db.connect('wikidatawiki') as cur:
    cur.execute(query)
    data = cur.fetchall()

output = ''
for _id, desc in data:
    output += make_link(_id)
    output += desc
    output += '<br />'

with open(os.path.expanduser('~/public_html/periods.html'), 'w') as f:
    f.write(output)
