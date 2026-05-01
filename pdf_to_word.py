#!/usr/bin/env python3
import os
import fitz  # PyMuPDF
from docx import Document
from docx.shared import Inches

# 输入和输出文件路径
input_path = '/root/.openclaw/media/inbound/ã_è_å_5å¹_é_è_æ_è_ç_ç_30ç_æ_ç_ã---a403e450-2162-4e6f-b31c-cc9b84db7b02.pdf'
output_path = '/root/.openclaw/workspace/articles.docx'

print(f"正在读取 PDF: {input_path}")

# 打开 PDF
doc = fitz.open(input_path)

print(f"总页数: {len(doc)}")

# 创建 Word 文档
document = Document()

for page_num in range(len(doc)):
    print(f"处理第 {page_num + 1} 页...")
    
    page = doc[page_num]
    
    # 提取文本
    text = page.get_text()
    
    # 添加到 Word 文档
    if text.strip():
        document.add_paragraph(text)
    
    # 每页之间加分页符
    if page_num < len(doc) - 1:
        document.add_page_break()

doc.close()

print("正在保存 Word 文档...")

# 保存 Word 文档
document.save(output_path)

print(f"完成！Word 文档保存在: {output_path}")
print(f"文件大小: {os.path.getsize(output_path) / 1024:.2f} KB")
