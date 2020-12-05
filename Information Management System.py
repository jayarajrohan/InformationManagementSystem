import sqlite3
import hashlib
import eel
from datetime import datetime, date


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


eel.start('index.html', size=(1000, 700))
