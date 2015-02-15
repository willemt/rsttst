#!/usr/bin/env python
# Author: Willem Thiart <himself@willemthiart.com>
# Copyright: Willem Thiart 2014

import locale
import re
from docutils import nodes, writers
from docutils.core import publish_cmdline, default_description
import codecs
import collections
import subprocess

try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass


class Dotted(object):
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return repr(self.s)

    def __str__(self):
        return str(self.s)

    def _cmp(self, b):
        from itertools import izip_longest
        lines = []
        for a, b in izip_longest(self.s.splitlines(), b.splitlines()):
            if b:
                def dotcompare(a, b):
                    dots = i = j = 0
                    while True:
                        try:
                            c1 = a[i]
                        except (IndexError, TypeError):
                            c1 = ''

                        try:
                            c2 = b[j]
                        except (IndexError, TypeError):
                            c2 = ''
                            if 3 == dots:
                                i += 1

                        if c1 == '' and c2 == '':
                            break

                        if c1 == '.':
                            dots += 1
                            i += 1
                        elif c1 == c2 and c1 != '.':
                            dots = 0
                            i += 1
                        elif 3 == dots:
                            pass
                        elif c1 != c2:
                            i += 1
                            j += 1
                            yield c1
                            continue
                        j += 1
                        yield c2
                lines.append(u"".join(dotcompare(a, b)))
            else:
                lines.append(a)
        self.s = u"\n".join(lines)
        return cmp(self.s, b)

    def __cmp__(self, other):
        return self._cmp(other)

    def __lt__(self, other):
        return self._cmp(other) < 0

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __eq__(self, other):
        return self._cmp(other) == 0

    def __ne__(self, other):
        return self._cmp(other) != 0

    def __gt__(self, other):
        return 0 < self._cmp(other)

    def __ge__(self, other):
        return 0 <= self._cmp(other)


def pythonify_title(title):
    mapping = {
        '+': 'plus',
        ' ': '_',
        '=': 'equals',
        }
    for k, v in mapping.items():
        title = title.replace(k, v)
    return ''.join(e for e in title if e.isalnum() or e == '_').lower()


def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8').strip().replace('\r', '')


class RstTstWriter(writers.Writer):
    supported = ('manpage',)
    """Formats this writer supports."""

    output = None
    """Final translated form of `document`."""

    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = Translator
        self.current_test = 'default'

    def translate(self):
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.astext()
        filename = 'test_{0}.py'.format(self.document.settings._source.lower().replace('.rst', ''))
        f = codecs.open(filename, 'w', 'utf-8')
        f.write(u"""# -*- coding: utf-8 -*-
from rsttst.core import run, Dotted

""")
        for i, block in enumerate(visitor.blocks):
            title = i
            if hasattr(block, 'title'):
                title = block.title
            f.write(u'def test_{0}():\n'.format(title))
            text_in = block.input.astext()
            text_in = re.sub(r'\\(\S)', r'\\\\\1', text_in)
            f.write(u'    output = run(u"""{0}""")\n'.format(text_in))
            text_out = block.output.astext()
            text_out = re.sub(r'\\(\S)', r'\\\\\1', text_out)
            text_out = text_out.replace('"""', '\\"""').strip()
            if 'dotted' in block.classes:
                f.write(u'    expected = Dotted(u"""{0}""")\n'.format(text_out))
                f.write(u'    cmp(output, expected)\n')
                f.write(u'    expected = u"{0}".format(expected)\n')
                f.write(u'    assert output == expected\n')
            else:
                f.write(u'    assert output == u"""{0}"""\n'.format(text_out))
            f.write(u'\n')
        f.write(u'if __name__ == "__main__": pass\n')


class Block(object):
    pass


class Translator(nodes.NodeVisitor):
    """"""

    words_and_spaces = re.compile(r'\S+| +|\n')
    possibly_a_roff_command = re.compile(r'\.\w')
    document_start = """Tests generated from reStructuredText."""

    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        self.blocks = []
        self.current_block = None
        self.current_title = None
        self.titles = collections.defaultdict(lambda: 0)

    def astext(self):
        return ''

    def visit_Text(self, node):
        pass

    def depart_Text(self, node):
        pass

    def visit_address(self, node):
        pass

    def depart_address(self, node):
        pass

    def visit_admonition(self, node, name=None):
        pass

    def depart_admonition(self, node):
        pass

    def visit_attention(self, node):
        pass

    def visit_docinfo_item(self, node, name):
        pass

    def depart_docinfo_item(self, node):
        pass

    def visit_author(self, node):
        pass

    def visit_authors(self, node):
        pass

    def depart_authors(self, node):
        pass

    def visit_block_quote(self, node):
        pass

    def depart_block_quote(self, node):
        pass

    def visit_bullet_list(self, node):
        pass

    def depart_bullet_list(self, node):
        pass

    def visit_caption(self, node):
        pass

    def depart_caption(self, node):
        pass

    def visit_caution(self, node):
        pass

    def visit_citation(self, node):
        pass

    def depart_citation(self, node):
        pass

    def visit_citation_reference(self, node):
        pass

    def visit_classifier(self, node):
        pass

    def depart_classifier(self, node):
        pass

    def visit_colspec(self, node):
        pass

    def depart_colspec(self, node):
        pass

    def write_colspecs(self):
        pass

    def visit_comment(self, node, sub=None):
        pass

    def visit_contact(self, node):
        pass

    def visit_container(self, node):
        pass

    def depart_container(self, node):
        pass

    def visit_compound(self, node):
        pass

    def depart_compound(self, node):
        pass

    def visit_copyright(self, node):
        pass

    def visit_danger(self, node):
        pass

    def visit_date(self, node):
        pass

    def visit_decoration(self, node):
        pass

    def depart_decoration(self, node):
        pass

    def visit_definition(self, node):
        pass

    def depart_definition(self, node):
        pass

    def visit_definition_list(self, node):
        pass

    def depart_definition_list(self, node):
        pass

    def visit_definition_list_item(self, node):
        pass

    def depart_definition_list_item(self, node):
        pass

    def visit_description(self, node):
        pass

    def depart_description(self, node):
        pass

    def visit_docinfo(self, node):
        pass

    def depart_docinfo(self, node):
        pass

    def visit_doctest_block(self, node):
        pass

    def depart_doctest_block(self, node):
        pass

    def visit_document(self, node):
        pass

    def depart_document(self, node):
        pass

    def visit_emphasis(self, node):
        pass

    def depart_emphasis(self, node):
        pass

    def visit_entry(self, node):
        pass

    def depart_entry(self, node):
        pass

    def visit_enumerated_list(self, node):
        pass

    def depart_enumerated_list(self, node):
        pass

    def visit_error(self, node):
        pass

    def visit_field(self, node):
        pass

    def depart_field(self, node):
        pass

    def visit_field_body(self, node):
        pass

    def depart_field_body(self, node):
        pass

    def visit_field_list(self, node):
        pass

    def depart_field_list(self, node):
        pass

    def visit_field_name(self, node):
        pass

    def depart_field_name(self, node):
        pass

    def visit_figure(self, node):
        pass

    def depart_figure(self, node):
        pass

    def visit_footer(self, node):
        pass

    def depart_footer(self, node):
        pass

    def visit_footnote(self, node):
        pass

    def depart_footnote(self, node):
        pass

    def footnote_backrefs(self, node):
        pass

    def visit_footnote_reference(self, node):
        pass

    def depart_footnote_reference(self, node):
        pass

    def visit_generated(self, node):
        pass

    def depart_generated(self, node):
        pass

    def visit_header(self, node):
        pass

    def depart_header(self, node):
        pass

    def visit_hint(self, node):
        pass

    def visit_inline(self, node):
        pass

    def depart_inline(self, node):
        pass

    def visit_subscript(self, node):
        pass

    def depart_subscript(self, node):
        pass

    def visit_superscript(self, node):
        pass

    def depart_superscript(self, node):
        pass

    def visit_attribution(self, node):
        pass

    def depart_attribution(self, node):
        pass

    def visit_image(self, node):
        pass

    def depart_image(self, node):
        pass

    def visit_important(self, node):
        pass

    def visit_label(self, node):
        pass

    def depart_label(self, node):
        pass

    def visit_legend(self, node):
        pass

    def depart_legend(self, node):
        pass

    def visit_line_block(self, node):
        pass

    def depart_line_block(self, node):
        pass

    def visit_line(self, node):
        pass

    def depart_line(self, node):
        pass

    def visit_list_item(self, node):
        pass

    def depart_list_item(self, node):
        pass

    def visit_literal(self, node):
        pass

    def depart_literal(self, node):
        pass

    def visit_literal_block(self, node):
        if not self.current_block:
            self.current_block = Block()
            self.current_block.input = node
            self.blocks.append(self.current_block)

            title = self.current_title
            self.titles[title] += 1
            if 1 < self.titles[title]:
                title = '{0}__{1}'.format(title, self.titles[title])
            self.current_block.title = title
        else:
            self.current_block.classes = node.attributes['classes']
            self.current_block.output = node
            self.current_block = None

    def depart_literal_block(self, node):
        pass

    def visit_math(self, node):
        pass

    def depart_math(self, node):
        pass

    def visit_math_block(self, node):
        pass

    def depart_math_block(self, node):
        pass

    def visit_meta(self, node):
        pass

    def depart_meta(self, node):
        pass

    def visit_note(self, node):
        pass

    def indent(self, by=0.5):
        pass

    def dedent(self):
        pass

    def visit_option_list(self, node):
        pass

    def depart_option_list(self, node):
        pass

    def visit_option_list_item(self, node):
        pass

    def depart_option_list_item(self, node):
        pass

    def visit_option_group(self, node):
        pass

    def depart_option_group(self, node):
        pass

    def visit_option(self, node):
        pass

    def depart_option(self, node):
        pass

    def visit_option_string(self, node):
        pass

    def depart_option_string(self, node):
        pass

    def visit_option_argument(self, node):
        pass

    def depart_option_argument(self, node):
        pass

    def visit_organization(self, node):
        pass

    def depart_organization(self, node):
        pass

    def first_child(self, node):
        pass

    def visit_paragraph(self, node):
        pass

    def depart_paragraph(self, node):
        pass

    def visit_problematic(self, node):
        pass

    def depart_problematic(self, node):
        pass

    def visit_raw(self, node):
        pass

    def visit_reference(self, node):
        pass

    def depart_reference(self, node):
        pass

    def visit_revision(self, node):
        pass

    def visit_row(self, node):
        pass

    def depart_row(self, node):
        pass

    def visit_section(self, node):
        pass

    def depart_section(self, node):
        pass

    def visit_status(self, node):
        pass

    def visit_strong(self, node):
        pass

    def depart_strong(self, node):
        pass

    def visit_substitution_definition(self, node):
        pass

    def visit_substitution_reference(self, node):
        pass

    def visit_subtitle(self, node):
        pass

    def depart_subtitle(self, node):
        pass

    def visit_system_message(self, node):
        pass

    def depart_system_message(self, node):
        pass

    def visit_table(self, node):
        pass

    def depart_table(self, node):
        pass

    def visit_target(self, node):
        pass

    def depart_target(self, node):
        pass

    def visit_tbody(self, node):
        pass

    def depart_tbody(self, node):
        pass

    def visit_term(self, node):
        pass

    def depart_term(self, node):
        pass

    def visit_tgroup(self, node):
        pass

    def depart_tgroup(self, node):
        pass

    def visit_thead(self, node):
        pass

    def depart_thead(self, node):
        pass

    def visit_tip(self, node):
        pass

    def visit_title(self, node):
        title = pythonify_title(node.astext())
        self.current_title = title

    def depart_title(self, node):
        pass

    def visit_title_reference(self, node):
        pass

    def depart_title_reference(self, node):
        pass

    def visit_topic(self, node):
        pass

    def depart_topic(self, node):
        pass

    def visit_sidebar(self, node):
        pass

    def depart_sidebar(self, node):
        pass

    def visit_rubric(self, node):
        pass

    def depart_rubric(self, node):
        pass

    def visit_transition(self, node):
        pass

    def depart_transition(self, node):
        pass

    def visit_version(self, node):
        pass

    def visit_warning(self, node):
        pass

    def unimplemented_visit(self, node):
        pass


def main():
    description = ("Generates test code.  " + default_description)
    publish_cmdline(writer=RstTstWriter(), description=description)


if __name__ == '__main__':
    main()

# vim: set fileencoding=utf-8 et ts=4 ai :
