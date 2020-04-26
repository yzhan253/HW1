# -*- coding: utf-8 -*-

from lxml import etree
import sys


def get_books_info(html):
    books_info_result = []
    with open(html, encoding='utf-8') as fr:
        text = fr.read()
    books_html = etree.HTML(text)
    all_books_nodes = books_html.xpath('//div[@class="AllEditionsItem-tile Recipe-default"]')
    for book_node in all_books_nodes:
        tmp_book = {}
        book_title_authot_node = book_node.xpath('./div')[0].xpath('./div')
        book_title = book_title_authot_node[0].xpath('./a')[0].text
        tmp_book['title'] = book_title
        if book_title_authot_node[1].xpath('./a'):
            book_authors = book_title_authot_node[1].xpath('./a')[0].text
        else:
            book_authors = None
        tmp_book['authors'] = book_authors
        book_price_node = book_node.xpath('./div')[1].xpath('./div/div')[1].xpath('./div')
        book_price_node = book_price_node[0].xpath('./div')[0].xpath('./div[@class="SearchResultListItem-dollarAmount"]')
        if book_price_node:
            book_price = book_price_node[0].text
        else:
            book_price = '0.0'
        tmp_book['price'] = book_price
        format_condition_node = book_node.xpath('./div')[1].xpath('./div/div')[1].xpath('./div')
        if len(format_condition_node) == 2:
            format_node = format_condition_node[1].xpath('./div')[0]
            condition_node = format_condition_node[1].xpath('./div')[1]
            book_format = format_node.xpath('./strong/text()')[0]
            book_condition = condition_node.xpath('./strong/text()')[0]
        else:
            book_format = None
            book_condition = None
        tmp_book['format'] = book_format
        tmp_book['condition'] = book_condition
        books_info_result.append(tmp_book)
    return books_info_result


def write_xml_file(books_info_result, xml):
    fw = open(xml, 'w')
    fw.writelines(['<?xml version="1.0"?>\n', '<books>\n'])
    count = 1
    for book in books_info_result:
        lines = ['\t<book>\n', '\t\t<id>' + str(count) + '</id>\n']
        for key, value in book.items():
            lines.append('\t\t' + '<' + key + '>' + str(value) + '</' + key + '>\n')
        lines.append('\t</book>\n')
        count += 1
        fw.writelines(lines)
    fw.write('</books>')
    fw.close()


if __name__ == '__main__':
    html = sys.argv[1]
    xml = sys.argv[2]
    books_info_result = get_books_info(html)
    write_xml_file(books_info_result, xml)