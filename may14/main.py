from chatWithPDF import ChatWithPDF

def main():
    chat = ChatWithPDF()

    print("=== ChatWithPDF CLI ===")
    print("Commands:")
    print("  /upload <path_to_pdf>  - Upload and process a new PDF")
    print("  /list                  - List available PDFs")
    print("  /select <pdf_name>     - Select a PDF to chat with")
    print("  /ask <question>        - Ask a question")
    print("  /exit                  - Exit the application")
    print("========================\n")

    while True:
        user_input = input(">> ").strip()

        if user_input.startswith("/upload "):
            path = user_input[len("/upload "):].strip()
            try:
                chat.upload_pdf(path)
                print(f"[✓] Uploaded and indexed: {path}")
            except Exception as e:
                print(f"[!] Error: {e}")

        elif user_input == "/list":
            if chat.availablePDFs:
                print("Available PDFs:")
                for pdf in chat.availablePDFs:
                    print(f"  - {pdf}")
            else:
                print("[!] No PDFs available. Upload one using /upload <path>")

        elif user_input.startswith("/select "):
            name = user_input[len("/select "):].strip()
            if name in chat.availablePDFs:
                chat.currentPDF = name
                print(f"[✓] Selected PDF: {name}")
            else:
                print(f"[!] PDF '{name}' not found in log.")

        elif user_input.startswith("/ask "):
            if not chat.currentPDF:
                print("[!] No PDF selected. Use /select <pdf_name> first.")
                continue
            question = user_input[len("/ask "):].strip()
            try:
                answer = chat.ask_question(question)
                print(f"PDF boat\n \t {answer}")
            except Exception as e:
                print(f"[!] Error during answer: {e}")

        elif user_input == "/exit":
            print("Exiting ChatWithPDF CLI.")
            break

        else:
            print("[!] Unknown command. Use /upload, /list, /select, /ask, or /exit.")

if __name__ == "__main__":
    main()
