#!/usr/bin/env python3
import os
import fitz  # PyMuPDF

# 输入和输出文件路径
input_path = '/root/.openclaw/media/inbound/ã_è_å_5å¹_é_è_æ_è_ç_ç_30ç_æ_ç_ã---e664f5c5-b560-478e-85ee-0c3c3757bcf3.pdf'
output_path = '/root/.openclaw/workspace/processed_articles_v2.pdf'

print(f"正在读取 PDF: {input_path}")

# 打开 PDF
doc = fitz.open(input_path)

print(f"总页数: {len(doc)}")

# 页脚文本
footer_text = "更多系统学习加微信 jkchen767676"

for page_num in range(len(doc)):
    print(f"处理第 {page_num + 1} 页...")
    
    page = doc[page_num]
    rect = page.rect
    
    # 定义页眉和页脚区域（假设页眉在顶部 80 像素，页脚在底部 80 像素）
    # 这需要根据实际 PDF 调整
    header_rect = fitz.Rect(0, 0, rect.width, 80)
    footer_rect = fitz.Rect(0, rect.height - 80, rect.width, rect.height)
    
    # 去掉页眉和页脚区域的内容
    # 用白色背景覆盖
    page.draw_rect(header_rect, color=(1, 1, 1), fill=(1, 1, 1))
    page.draw_rect(footer_rect, color=(1, 1, 1), fill=(1, 1, 1))
    
    # 添加新的页脚
    # 在底部居中位置添加文本
    text_length = fitz.get_text_length(footer_text, fontname="Helvetica", fontsize=10)
    x = (rect.width - text_length) / 2
    y = rect.height - 30  # 距离底部 30 像素
    
    page.insert_text((x, y), footer_text, fontsize=10, color=(0.5, 0.5, 0.5))

print("正在保存处理后的 PDF...")

# 保存输出文件
doc.save(output_path)
doc.close()

print(f"完成！处理后的 PDF 保存在: {output_path}")
print(f"文件大小: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")
