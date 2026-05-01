#!/usr/bin/env python3
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import io

# 输入和输出文件路径
input_path = '/root/.openclaw/media/inbound/ã_è_å_5å¹_é_è_æ_è_ç_ç_30ç_æ_ç_ã---e664f5c5-b560-478e-85ee-0c3c3757bcf3.pdf'
output_path = '/root/.openclaw/workspace/processed_articles.pdf'

print(f"正在读取 PDF: {input_path}")

# 读取原始 PDF
reader = PdfReader(input_path)
writer = PdfWriter()

print(f"总页数: {len(reader.pages)}")

# 页脚文本
footer_text = "更多系统学习加微信 jkchen767676"

for page_num in range(len(reader.pages)):
    print(f"处理第 {page_num + 1} 页...")
    
    # 获取原始页面
    page = reader.pages[page_num]
    
    # 获取页面尺寸
    page_width = float(page.mediabox.width)
    page_height = float(page.mediabox.height)
    
    # 创建一个新的 PDF 来绘制页脚
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    
    # 设置页脚样式
    can.setFont("Helvetica", 10)
    can.setFillColor(colors.grey)
    
    # 计算页脚位置（底部居中）
    text_width = can.stringWidth(footer_text, "Helvetica", 10)
    x = (page_width - text_width) / 2
    y = 30  # 距离底部 30 个单位
    
    # 绘制页脚
    can.drawString(x, y, footer_text)
    can.save()
    
    # 移动到开始并读取这个新的 PDF
    packet.seek(0)
    new_pdf = PdfReader(packet)
    
    # 将页脚合并到原始页面
    page.merge_page(new_pdf.pages[0])
    
    # 添加到输出
    writer.add_page(page)

print("正在保存处理后的 PDF...")

# 保存输出文件
with open(output_path, "wb") as f:
    writer.write(f)

print(f"完成！处理后的 PDF 保存在: {output_path}")
print(f"文件大小: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")
