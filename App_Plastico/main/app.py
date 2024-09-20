# main/app.py
import tkinter as tk
from database.connection import create_connection
from database.tables import create_tables
from gui.screens import AppScreens
import config.settings as settings  # Asegúrate de que esto sea correcto

def main():
    root = tk.Tk()

    conn = create_connection()
    if conn is None:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conn.cursor()
    create_tables(cursor)
    conn.commit()

    app = AppScreens(root, cursor, conn)
    root.mainloop()

if __name__ == "__main__":
    main()
