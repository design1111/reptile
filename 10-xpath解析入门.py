from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周dada</nick>
        <nick class="joy">jiejie</nick>
        <nick class="jolin">kekek</nick>
        <div>
            <nick>rere</nick>
        </div>
        <span>
            <nick>rere23222</nick>
        </span>
    </author>
    <partner>
        <nick id="ppc">oppp</nick>
        <nick id="pljk">nhjfdf</nick>
    </partner>
</book>
"""
tree = etree.XML(xml)
result1 = tree.xpath("/book")  # /表示层级关系，第一个/是根节点
result2 = tree.xpath("/book/name/text()")  #text()拿文本
result3 = tree.xpath("/book/author//nick/text()")  #拿取author中的所有nick；包含div中的nick
print(result3)
result4 = tree.xpath("/book/author/*/nick/text()")  #* 任意的节点，通配符
print(result4)