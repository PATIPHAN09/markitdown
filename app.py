import gradio as gr
from markitdown import MarkItDown

md = MarkItDown()


def convert_file(file):
    if file is None:
        return "กรุณาอัปโหลดไฟล์"
    try:
        result = md.convert(file.name)
        return result.text_content
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {e}"


with gr.Blocks(title="MarkItDown UI") as app:
    gr.Markdown("# MarkItDown\nลากไฟล์มาวาง แล้วกด **แปลง** เพื่อได้ Markdown")

    with gr.Row():
        file_input = gr.File(label="อัปโหลดไฟล์")
        convert_btn = gr.Button("แปลงเป็น Markdown", variant="primary")

    output = gr.Textbox(label="ผลลัพธ์ Markdown", lines=25)

    convert_btn.click(fn=convert_file, inputs=file_input, outputs=output)

if __name__ == "__main__":
    app.launch()
