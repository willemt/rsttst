# -*- coding: utf-8 -*-
# Author: Willem Thiart
# Copyright: This module is put into the public domain.


__docformat__ = 'reStructuredText'

import sys
import re
from docutils import nodes, writers


class Writer(writers.Writer):

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
        out = open('test_{0}.py'.format(sys.argv[1].lower().replace('.rst', '')), 'w')
        out.write("""import pytest
import os
import subprocess
import sys
import shlex

def run(cmd):
    os.system(cmd)


""")
        
        for i, block in enumerate(visitor.blocks):
            title = i
            if hasattr(block, 'title'):
                title = block.title
            out.write('def test_{0}(capfd):\n'.format(title))
            for line in block.input.astext().splitlines():
                out.write('    run("""{0}""")\n'.format(line))
            text = block.output.astext().replace('"""', '\\"\\"\\"')
            out.write('    assert capfd.readouterr()[0] == """{0}\n"""\n'.format(text))
            out.write('\n')
        out.write('if __name__ == "__main__": pass\n')


class Block(object):
    pass


class Translator(nodes.NodeVisitor):
    """"""

    words_and_spaces = re.compile(r'\S+| +|\n')
    possibly_a_roff_command = re.compile(r'\.\w')
    document_start = """Man page generated from reStructuredText."""

    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        self.blocks = []
        self.current_block = None
        self.current_title = None

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
            self.blocks.append(self.current_block)
            self.current_block.input = node
            title = self.current_title
            mapping = {
                '+': 'plus',
                ' ': '_',
                '=': 'equals',
                }
            for k, v in mapping.iteritems():
                title = title.replace(k, v)
            title = ''.join(e for e in title if e.isalnum() or e == '_')
            self.current_block.title = title.lower()
            self.current_title = None
        else:
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
        self.current_title = node.astext()
        pass

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

# vim: set fileencoding=utf-8 et ts=4 ai :