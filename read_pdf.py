
import PyPDF2
import sys

def read_pdf_content(file_path, page_count=5):
    """
    读取PDF文件的文本内容
    :param file_path: PDF文件路径
    :param page_count: 需要读取的页数
    :return: 文本内容列表
    """
    content = []
    
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            print(f"PDF文件总页数: {len(pdf_reader.pages)}")
            print("-" * 50)
            
            for i in range(min(page_count, len(pdf_reader.pages))):
                page = pdf_reader.pages[i]
                text = page.extract_text()
                content.append(text)
                
                print(f"\n第 {i+1} 页内容:")
                print("-" * 50)
                print(text)
                
            print("\n" + "-" * 50)
            print("PDF内容读取完成")
            
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 未找到")
    except Exception as e:
        print(f"错误: 读取PDF文件时出现异常 - {e}")
    
    return content

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        page_count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        read_pdf_content(file_path, page_count)
    else:
        print("用法: python read_pdf.py <pdf_file_path> [page_count]")
