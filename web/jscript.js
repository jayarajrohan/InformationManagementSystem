function login_func()
{
	var username = document.getElementById("username").value;
	var pword = document.getElementById("pword").value;
	eel.login(username, pword)(set_login);
}

function set_login(result)
{
	if(result == "Failed")
	{
		window.alert("Please insert correct username and password");
	}
	else
	{
		eel.retrieve();
	}
}

function add_func()
{
	var NIC = document.getElementById("NIC").value;
	var Name = document.getElementById("Name").value;
	var DOB = document.getElementById("DOB").value;
	var Sex = document.getElementById("Sex").value;
	var Address = document.getElementById("Address").value;
	Address = Address.toString();
	Address = Address.replaceAll(',','*');
	var phone = document.getElementById("phone").value;
	var Of_name = document.getElementById("Of_name").value;
	var Mem_Number = document.getElementById("Mem_Number").value;
	var Mem_Date = document.getElementById("Mem_Date").value;
	eel.add(NIC, Name, DOB, Sex, Address, phone, Of_name, Mem_Number, Mem_Date)(set_add)
}

function set_add(fin)
{
	if(fin == "Found")
	{
		window.alert("Entered NIC already exist")
	}
}

function retrieve_func()
{
	var NIC = document.getElementById("NIC").value;
	eel.retrieved(NIC)(set_retrieve)
}

function set_retrieve(result)
{
	if(result == "Yes")
	{
		var NIC = document.getElementById("NIC").value;
		eel.retrieved_2(NIC)(set_retrieve_2)
	}
	else
	{
		window.alert("No Information available on this NIC")
	}
}

function set_retrieve_2(name)
{
	var rock = name.toString();
	var i;
	var arr = rock.split(",")
	var x = document.getElementsByClassName('jaguar');
	for(i = 0; i < x.length; i++) {
		x[i].value = arr[i].replaceAll("*",",");
	}
	window.stop();
}
function up_func()
{
	var NIC = document.getElementById("NIC").value;
	var Name = document.getElementById("Name").value;
	var DOB = document.getElementById("DOB").value;
	var Sex = document.getElementById("Sex").value;
	var Address = document.getElementById("Address").value;
	Address = Address.toString();
	Address = Address.replaceAll(',','*');
	var phone = document.getElementById("phone").value;
	var Of_name = document.getElementById("Of_name").value;
	var Mem_Number = document.getElementById("Mem_Number").value;
	var Mem_Date = document.getElementById("Mem_Date").value;
	eel.update(NIC, Name, DOB, Sex, Address, phone, Of_name, Mem_Number, Mem_Date)(set_update)
}
function set_update(result)
{
	if(result == "Not updated")
	{
		window.alert("NIC you entered is not available or You can't change the NIC! plese consider DELETING")
	}
}
function del_func()
{
	var NIC = document.getElementById("NIC").value;
	eel.delete_func(NIC)(set_delete);
}
function set_delete(result)
{
	if(result == "Not deleted")
	{
		window.alert("Entered NIC is not exist to delete");
	}
}
function change_user_func()
{
	var CUN = document.getElementById("CUN").value
	var NUN = document.getElementById("NUN").value
	var CNUN = document.getElementById("CNUN").value
	var pw = document.getElementById("pw").value
	if(NUN != CNUN)
	{
		window.alert("New Usernames don't match");
	}
	else
	{
		eel.change_username(CUN, pw, NUN)(set_change_username)
	}
}
function set_change_username(result)
{
	if (result == "Wrong username")
	{
		window.alert("Entered current username is wrong");
	}
	else if (result == "Wrong password")
	{
		window.alert("Entered password is wrong")
	}
}
function change_pass_func()
{
	var CUP = document.getElementById("CUP").value
	var NPW = document.getElementById("NPW").value
	var CNPW = document.getElementById("CNPW").value
	if(NPW != CNPW)
	{
		window.alert("New passwords don't match")
	}
	else
	{
		eel.change_password(CUP, NPW)(set_change_password)
	}
}
function set_change_password(result)
{
	if(result == "Wrong password")
	{
		window.alert("Entered current password is wrong");
	}
}