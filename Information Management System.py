import sqlite3
import hashlib
import eel
from datetime import datetime, date
import csv
import os
import tkinter
from tkinter import filedialog
from docx import Document

eel.init('web')


def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


@eel.expose
def login(username, password):
    username = username
    password = encrypt_string(password)

    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM login WHERE username= ? and password= ?", (username, password))
    found = c.fetchone()

    if found:
        result = "Successful"
    else:
        result = "Failed"

    conn.close()
    return result


@eel.expose
def retrieve():
    eel.start('retrieve.html', size=(1000, 700), port=8001)


@eel.expose
def add(nic, name, dob, sex, address, phone, of_name, mem_number, mem_date):
    nic = str(nic)
    nic = nic.lower()

    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute(('''CREATE TABLE IF NOT EXISTS info(NIC text PRIMARY KEY, name text, 
    DOB text, sex text, address text, phone text, of_name text, mem_number text, mem_date text)'''))
    conn.commit()
    conn.close()

    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM info WHERE NIC= ?", [nic])
    found = c.fetchone()

    if found:
        result = "Found"
        return result
    else:
        c.execute("INSERT INTO info(NIC, name, DOB, sex, address, phone, "
                  "of_name, mem_number, mem_date) values (?, ?, ?, ?, ?, ?, ?,"
                  " ?, ?)", (nic, name, dob, sex, address, phone, of_name, mem_number, mem_date))
        conn.commit()
        conn.close()
        result = "Not found"
        return result


@eel.expose
def retrieved(nic):
    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM info WHERE NIC= ?", [nic])
    found = c.fetchone()
    if found:
        result = "Yes"
        return result
    else:
        result = "No"
        conn.commit()
        conn.close()
        return result


@eel.expose
def retrieved_2(nic):
    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM info WHERE NIC= ?", [nic])
    found = c.fetchone()

    if found:
        c = conn.cursor()
        c.execute("SELECT name FROM info WHERE NIC= ?", [nic])
        name = c.fetchone()

        c = conn.cursor()
        c.execute("SELECT DOB FROM info WHERE NIC= ?", [nic])
        dob = c.fetchone()

        age = str(dob)
        age = age.replace("-", " ")
        age = age.replace(",", "")
        age = age.replace("'", "")
        age = age.replace("(", "")
        age = age.replace(")", "")

        born = datetime.strptime(age, "%Y %m %d")
        today = date.today()
        age2 = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        c = conn.cursor()
        c.execute("SELECT sex FROM info WHERE NIC= ?", [nic])
        sex = c.fetchone()

        c = conn.cursor()
        c.execute("SELECT address FROM info WHERE NIC= ?", [nic])
        address = c.fetchone()

        c = conn.cursor()
        c.execute("SELECT phone FROM info WHERE NIC= ?", [nic])
        phone = c.fetchone()

        c = conn.cursor()
        c.execute("SELECT of_name FROM info WHERE NIC= ?", [nic])
        of_name = c.fetchone()

        c = conn.cursor()
        c.execute("SELECT mem_number FROM info WHERE NIC= ?", [nic])
        mem_number = c.fetchone()

        c = conn.cursor()
        c.execute("SELECT mem_date FROM info WHERE NIC= ?", [nic])
        mem_date = c.fetchone()

        conn.commit()
        conn.close()
        return name, dob, age2, sex, address, phone, of_name, mem_number, mem_date


@eel.expose()
def update(nic, name, dob, sex, address, phone, of_name, mem_number, mem_date):
    nic = str(nic)
    nic = nic.lower()

    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM info WHERE NIC= ?", [nic])
    found = c.fetchone()

    if found:
        c = conn.cursor()
        c.execute(''' UPDATE info SET name=?, DOB=?, sex=?, address=?, phone=?, 
        of_name=?, mem_number=?, mem_date=? WHERE NIC=?''', (name, dob, sex, address,
                  phone, of_name, mem_number, mem_date, nic))

        result = "Updated"

        conn.commit()
        conn.close()
        return result
    else:
        result = "Not updated"

        conn.close()
        return result


@eel.expose
def delete_func(nic):
    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM info WHERE NIC= ?", [nic])
    found = c.fetchone()

    if found:
        c = conn.cursor()
        c.execute('DELETE FROM info WHERE NIC=?', ([nic]))
        conn.commit()
        conn.close()

        result = "Deleted"
        return result
    else:
        result = "Not deleted"
        return result


@eel.expose
def change_username(current_username, current_password, new_username):
    current_pass = encrypt_string(current_password)

    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM login WHERE username=?", [current_username])
    found = c.fetchone()

    if found:
        c = conn.cursor()
        c.execute("SELECT password FROM login WHERE username=?", [current_username])
        found2 = c.fetchone()

        if found2:
            found2 = str(found2)
            found2 = found2.replace("(", "")
            found2 = found2.replace(")", "")
            found2 = found2.replace("'", "")
            found2 = found2.replace(",", "")

            if found2 == current_pass:
                c = conn.cursor()
                c.execute(''' UPDATE login SET username=? WHERE username=?''', (new_username, current_username))

                result = "Updated"

                conn.commit()
                conn.close()
                return result
            else:
                result = "Wrong password"

                conn.commit()
                conn.close()
                return result
    else:
        result = "Wrong username"

        conn.commit()
        conn.close()
        return result


@eel.expose
def change_password(current_password, new_password):
    current_pass = encrypt_string(current_password)
    new_pass = encrypt_string(new_password)

    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT username FROM login WHERE password=?", [current_pass])
    found = c.fetchone()

    if found:
        c = conn.cursor()
        c.execute(''' UPDATE login SET password=? WHERE password=?''', (new_pass, current_pass))

        result = "Updated"

        conn.commit()
        conn.close()
        return result
    else:
        result = "Wrong password"

        conn.commit()
        conn.close()
        return result


@eel.expose
def view():
    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute('SELECT * FROM info')
    records = c.fetchall()
    return records


@eel.expose
def export_info():
    cwd = os.getcwd()

    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM info")

    root = tkinter.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    dir_name = filedialog.askdirectory()

    if dir_name != '':
        os.chdir(dir_name)
        with open("Members_Info.csv", "w") as csv_file:
            rows = c.fetchall()
            for row in rows:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(row)

            result = "Successful"

            os.chdir(cwd)
            return result
    else:
        result = "Not successful"
        return result


@eel.expose
def ent_pay(nic, year, month, amount):
    conn = sqlite3.connect(year)
    c = conn.cursor()
    c.execute(('''CREATE TABLE IF NOT EXISTS contribution(NIC text, name text, of_name text, 
    January INTEGER DEFAULT 0, February INTEGER DEFAULT 0, March INTEGER DEFAULT 0, April INTEGER DEFAULT 0, 
    May INTEGER DEFAULT 0, June INTEGER DEFAULT 0, July INTEGER DEFAULT 0, August INTEGER DEFAULT 0, 
    September INTEGER DEFAULT 0, October INTEGER DEFAULT 0, November INTEGER DEFAULT 0, December INTEGER DEFAULT 0, 
    Total INTEGER DEFAULT 0)'''))
    conn.commit()

    c = conn.cursor()
    c.execute(('''CREATE TABLE IF NOT EXISTS month_total(NIC text, name text, of_name text, 
    January INTEGER DEFAULT 0, February INTEGER DEFAULT 0, March INTEGER DEFAULT 0, April INTEGER DEFAULT 0, 
    May INTEGER DEFAULT 0, June INTEGER DEFAULT 0, July INTEGER DEFAULT 0, August INTEGER DEFAULT 0, 
    September INTEGER DEFAULT 0, October INTEGER DEFAULT 0, November INTEGER DEFAULT 0, December INTEGER DEFAULT 0, 
    Total INTEGER DEFAULT 0)'''))
    conn.commit()

    c = conn.cursor()
    c.execute("SELECT * FROM month_total WHERE NIC= ?", ["Total"])
    available = c.fetchone()

    if not available:
        var1 = "Total"
        var2 = ""
        var3 = ""

        conn.cursor()
        c.execute("INSERT INTO month_total(NIC, name, of_name) values(?, ?, ?)", (var1, var2, var3))
        conn.commit()

    conn.close()

    conn2 = sqlite3.connect("information_database")
    c2 = conn2.cursor()
    c2.execute("SELECT name FROM info WHERE NIC= ?", [nic])
    name = c2.fetchone()

    c2 = conn2.cursor()
    c2.execute("SELECT of_name FROM info WHERE NIC= ?", [nic])
    office_name = c2.fetchone()

    if name:
        name = ((((str(name)).replace("(", "")).replace(")", "")).replace(",", "")).replace("'", "")
        office_name = ((((str(office_name)).replace("(", "")).replace(")", "")).replace(",", "")).replace("'", "")
        conn = sqlite3.connect(year)
        c = conn.cursor()
        c.execute("SELECT NIC FROM contribution WHERE NIC= ?", [nic])
        entry = c.fetchone()

        if entry:
            result = "Updated"

            c = conn.cursor()
            c.execute(''' UPDATE contribution SET %s= ? WHERE NIC=?''' % month, (int(amount), str(nic)))
            conn.commit()

            current_total = 0

            c = conn.cursor()
            c.execute("SELECT January FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT February FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT March FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT April FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT May FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT June FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT July FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT August FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT September FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT October FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT November FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT December FROM contribution WHERE NIC= ?", [nic])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute(''' UPDATE contribution SET Total= ? WHERE NIC=?''', (int(current_total), str(nic)))
            conn.commit()

            c = conn.cursor()
            c.execute("SELECT %s from contribution" % month)
            monthly_total = c.fetchall()

            temp_total = 0

            for j in monthly_total:
                j = str(j)
                j = ((j.replace("(", "")).replace(")", "")).replace(",", "")
                j = int(j)
                temp_total += j

            c = conn.cursor()
            c.execute(''' UPDATE month_total SET %s= ? WHERE NIC=?''' % month, (int(temp_total), str("Total")))
            conn.commit()

            current_total = 0

            c = conn.cursor()
            c.execute("SELECT January FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT February FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT March FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT April FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT May FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT June FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT July FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT August FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT September FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT October FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT November FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT December FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute(''' UPDATE month_total SET Total= ? WHERE NIC=?''', (int(current_total), str("Total")))
            conn.commit()

            conn.close()
            conn2.close()
            return result

        else:
            result = "Inserted"

            c = conn.cursor()
            c.execute("INSERT INTO contribution(NIC, name, of_name, %s, Total) values (?, ?, ?, "
                      "?, ?)" % month, (str(nic), str(name), str(office_name), int(amount), int(amount)))
            conn.commit()

            c = conn.cursor()
            c.execute("SELECT %s from contribution" % month)
            monthly_total = c.fetchall()

            temp_total = 0

            for j in monthly_total:
                j = str(j)
                j = ((j.replace("(", "")).replace(")", "")).replace(",", "")
                j = int(j)
                temp_total += j

            c = conn.cursor()
            c.execute(''' UPDATE month_total SET %s= ? WHERE NIC=?''' % month, (int(temp_total), str("Total")))
            conn.commit()

            current_total = 0

            c = conn.cursor()
            c.execute("SELECT January FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT February FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT March FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT April FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT May FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT June FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT July FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT August FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT September FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT October FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT November FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute("SELECT December FROM month_total WHERE NIC= ?", ["Total"])
            person_total = c.fetchone()
            person_total = str(person_total)
            person_total = ((person_total.replace("(", "")).replace(")", "")).replace(",", "")
            person_total = int(person_total)
            current_total += person_total

            c = conn.cursor()
            c.execute(''' UPDATE month_total SET Total= ? WHERE NIC=?''', (int(current_total), str("Total")))
            conn.commit()

            conn.close()
            conn2.close()
            return result
    else:
        result = "Not found"
        return result


@eel.expose
def year_mul_view(year):
    conn = sqlite3.connect(year)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type= 'table' AND name= 'contribution'")
    count = c.fetchone()
    if count:
        c = conn.cursor()
        c.execute("SELECT * FROM contribution WHERE NIC= ?", ["Total"])
        available = c.fetchone()
        if available:
            c = conn.cursor()
            c.execute("DELETE FROM contribution WHERE NIC= ?", ["Total"])
            conn.commit()

        nic = "Total"

        c = conn.cursor()
        c.execute("SELECT name FROM month_total WHERE NIC=?", [nic])
        name = c.fetchone()
        name = ((str(name).replace("(", "")).replace(")", "")).replace(",", "")

        c = conn.cursor()
        c.execute("SELECT of_name FROM month_total WHERE NIC=?", [nic])
        of_name = c.fetchone()
        of_name = ((str(of_name).replace("(", "")).replace(")", "")).replace(",", "")

        c = conn.cursor()
        c.execute("SELECT January FROM month_total WHERE NIC=?", [nic])
        january = c.fetchone()
        january = ((str(january).replace("(", "")).replace(")", "")).replace(",", "")
        january = int(january)

        c = conn.cursor()
        c.execute("SELECT February FROM month_total WHERE NIC=?", [nic])
        february = c.fetchone()
        february = ((str(february).replace("(", "")).replace(")", "")).replace(",", "")
        february = int(february)

        c = conn.cursor()
        c.execute("SELECT March FROM month_total WHERE NIC=?", [nic])
        march = c.fetchone()
        march = ((str(march).replace("(", "")).replace(")", "")).replace(",", "")
        march = int(march)

        c = conn.cursor()
        c.execute("SELECT April FROM month_total WHERE NIC=?", [nic])
        april = c.fetchone()
        april = ((str(april).replace("(", "")).replace(")", "")).replace(",", "")
        april = int(april)

        c = conn.cursor()
        c.execute("SELECT May FROM month_total WHERE NIC=?", [nic])
        may = c.fetchone()
        may = ((str(may).replace("(", "")).replace(")", "")).replace(",", "")
        may = int(may)

        c = conn.cursor()
        c.execute("SELECT June FROM month_total WHERE NIC=?", [nic])
        june = c.fetchone()
        june = ((str(june).replace("(", "")).replace(")", "")).replace(",", "")
        june = int(june)

        c = conn.cursor()
        c.execute("SELECT July FROM month_total WHERE NIC=?", [nic])
        july = c.fetchone()
        july = ((str(july).replace("(", "")).replace(")", "")).replace(",", "")
        july = int(july)

        c = conn.cursor()
        c.execute("SELECT August FROM month_total WHERE NIC=?", [nic])
        august = c.fetchone()
        august = ((str(august).replace("(", "")).replace(")", "")).replace(",", "")
        august = int(august)

        c = conn.cursor()
        c.execute("SELECT September FROM month_total WHERE NIC=?", [nic])
        september = c.fetchone()
        september = ((str(september).replace("(", "")).replace(")", "")).replace(",", "")
        september = int(september)

        c = conn.cursor()
        c.execute("SELECT October FROM month_total WHERE NIC=?", [nic])
        october = c.fetchone()
        october = ((str(october).replace("(", "")).replace(")", "")).replace(",", "")
        october = int(october)

        c = conn.cursor()
        c.execute("SELECT November FROM month_total WHERE NIC=?", [nic])
        november = c.fetchone()
        november = ((str(november).replace("(", "")).replace(")", "")).replace(",", "")
        november = int(november)

        c = conn.cursor()
        c.execute("SELECT December FROM month_total WHERE NIC=?", [nic])
        december = c.fetchone()
        december = ((str(december).replace("(", "")).replace(")", "")).replace(",", "")
        december = int(december)

        c = conn.cursor()
        c.execute("SELECT Total FROM month_total WHERE NIC=?", [nic])
        total = c.fetchone()
        total = ((str(total).replace("(", "")).replace(")", "")).replace(",", "")
        total = int(total)

        c = conn.cursor()
        c.execute("INSERT INTO contribution(NIC, name, of_name, January, February, March, April, May, June, July, "
                  "August, September, October, November, December, Total) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                  "?, ?, ?, ?, ?, ?)", (str(nic), str(name), str(of_name), int(january), int(february), int(march),
                                        int(april), int(may), int(june), int(july), int(august), int(september),
                                        int(october), int(november), int(december), int(total)))
        conn.commit()

        c = conn.cursor()
        c.execute('SELECT * FROM contribution')
        records = c.fetchall()
        if records:
            conn.close()
            return records
        else:
            result = "Not Found"
            return result
    else:
        result = "False"
        conn.close()
        return result


@eel.expose
def month_mul_view(year, month):
    conn = sqlite3.connect(year)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type= 'table' AND name= 'contribution'")
    count = c.fetchone()
    if count:
        c = conn.cursor()
        c.execute('SELECT NIC,name, of_name, %s FROM contribution' % month)
        records = c.fetchall()
        if records:
            conn.close()
            return records
        else:
            result = "Not Found"
            return result
    else:
        result = "False"
        conn.close()
        return result


@eel.expose
def year_sin_view(nic, year):
    conn = sqlite3.connect(year)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type= 'table' AND name= 'contribution'")
    count = c.fetchone()
    if count:
        c = conn.cursor()
        c.execute('SELECT * FROM contribution WHERE NIC =?', [nic])
        records = c.fetchone()
        if records:
            conn.close()
            return records
        else:
            result = "Not Found"
            return result
    else:
        result = "False"
        conn.close()
        return result


@eel.expose
def month_sin_view(nic, year, month):
    conn = sqlite3.connect(year)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type= 'table' AND name= 'contribution'")
    count = c.fetchone()
    if count:
        c = conn.cursor()
        c.execute('SELECT %s FROM contribution WHERE NIC= ?' % month, [nic])
        records = c.fetchall()
        if records:
            conn.close()
            return records
        else:
            result = "Not Found"
            return result
    else:
        result = "False"
        conn.close()
        return result


@eel.expose
def year_office_view(year, office):
    conn = sqlite3.connect(year)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type= 'table' AND name= 'contribution'")
    count = c.fetchone()

    if count:
        c = conn.cursor()
        c.execute('SELECT * FROM contribution WHERE of_name= ?', [office])
        records = c.fetchall()
        if records:
            conn.close()
            return records
        else:
            result = "Not Found"
            return result


@eel.expose
def month_office_view(year, month, office):
    conn = sqlite3.connect(year)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type= 'table' AND name= 'contribution'")
    count = c.fetchone()
    if count:
        c = conn.cursor()
        c.execute('SELECT NIC,name, of_name, %s FROM contribution WHERE of_name= ?' % month, [office])
        records = c.fetchall()
        if records:
            conn.close()
            return records
        else:
            result = "Not Found"
            return result
    else:
        result = "False"
        conn.close()
        return result


@eel.expose
def create_id(nic):
    conn = sqlite3.connect("information_database")
    c = conn.cursor()
    c.execute("SELECT * FROM info WHERE NIC= ?", [nic])
    found = c.fetchone()

    if found:

        result = "Found"
        return result
    else:
        result = "Not found"
        return result


eel.start('index.html', size=(1000, 700))
