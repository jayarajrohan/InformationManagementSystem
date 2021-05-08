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
	NIC = NIC.toString();
	NIC = NIC.replaceAll(',','*');
	var Name = document.getElementById("Name").value;
	Name = Name.toString();
	Name = Name.replaceAll(',','*');
	var DOB = document.getElementById("DOB").value;
	DOB = DOB.toString();
	DOB = DOB.replaceAll(',','*');
	var Sex = document.getElementById("Sex").value;
	Sex = Sex.toString();
	Sex = Sex.replaceAll(',','*');
	var Address = document.getElementById("Address").value;
	Address = Address.toString();
	Address = Address.replaceAll(',','*');
	var phone = document.getElementById("phone").value;
	phone = phone.toString();
	phone = phone.replaceAll(',','*');
	var Of_name = document.getElementById("Of_name").value;
	Of_name = Of_name.toString();
	Of_name = Of_name.replaceAll(',','*');
	var Mem_Number = document.getElementById("Mem_Number").value;
	Mem_Number = Mem_Number.toString();
	Mem_Number = Mem_Number.replaceAll(',','*');
	var Mem_Date = document.getElementById("Mem_Date").value;
	Mem_Date = Mem_Date.toString();
	Mem_Date = Mem_Date.replaceAll(',','*');
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
	NIC = NIC.toString();
	NIC = NIC.replaceAll(',','*');
	var Name = document.getElementById("Name").value;
	Name = Name.toString();
	Name = Name.replaceAll(',','*');
	var DOB = document.getElementById("DOB").value;
	DOB = DOB.toString();
	DOB = DOB.replaceAll(',','*');
	var Sex = document.getElementById("Sex").value;
	Sex = Sex.toString();
	Sex = Sex.replaceAll(',','*');
	var Address = document.getElementById("Address").value;
	Address = Address.toString();
	Address = Address.replaceAll(',','*');
	var phone = document.getElementById("phone").value;
	phone = phone.toString();
	phone = phone.replaceAll(',','*');
	var Of_name = document.getElementById("Of_name").value;
	Of_name = Of_name.toString();
	Of_name = Of_name.replaceAll(',','*');
	var Mem_Number = document.getElementById("Mem_Number").value;
	Mem_Number = Mem_Number.toString();
	Mem_Number = Mem_Number.replaceAll(',','*');
	var Mem_Date = document.getElementById("Mem_Date").value;
	Mem_Date = Mem_Date.toString();
	Mem_Date = Mem_Date.replaceAll(',','*');
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
function view_func()
{
	eel.view()(set_view)
}
function set_view(records)
{
	var i;
	for(i=0; i<records.length; i++)
	{
		var y = document.createElement("TR");
		y.setAttribute("id", i);
		document.getElementById("view_table").appendChild(y);
		for (j=0; j<records[i].length; j++)
		{
			var z = document.createElement("TD");
			var t = document.createTextNode(records[i][j].replaceAll("*", ","));
			z.appendChild(t);
			document.getElementById(i).appendChild(z);
		}
	}
}
function export_func()
{
	eel.export_info()(set_export_func)
}
function set_export_func(result)
{
	if (result == "Successful")
	{
		window.alert('Exported successfully');
	}
}
function pay_add()
{
	var NIC = document.getElementById("NIC").value
	var year = document.getElementById("year").value
	var month = document.getElementById("month").value
	var amount = document.getElementById("amount").value
	eel.ent_pay(NIC, year, month, amount)(set_pay_add)
}
function set_pay_add(result)
{
	if(result == "Not found")
	{
		window.alert('Entered NIC does not found');
	}
	document.getElementById("NIC").value = "";
	document.getElementById("NIC").placeholder = "Enter NIC";
	document.getElementById("amount").value = "";
	document.getElementById("amount").placeholder = "Enter Contribution";
	window.stop();
}
function view_pay_func()
{
	var NIC = document.getElementById("NIC").value;
	var year = document.getElementById("year").value;
	var month = document.getElementById("month").value;
	var of_name = document.getElementById("Of_name").value;
	of_name = of_name.replaceAll(",", "*")
	if(NIC == "" && month == "" && of_name == "")
	{
		eel.year_mul_view(year)(set_year_mul_view)
	}
	else if(NIC == "" && month != "" && of_name == "")
	{
		eel.month_mul_view(year, month)(set_month_mul_view)
	}
	else if(NIC != "" && month == "" && of_name == "")
	{
		eel.year_sin_view(NIC, year)(set_year_sin_view)
	}
	else if(month != "" && NIC != "" && of_name == "")
	{
		eel.month_sin_view(NIC, year, month)(set_month_sin_view)
	}
	else if(of_name != "" && month == "" && NIC == "")
	{
		eel.year_office_view(year, of_name)(set_year_office_view)
	}
	else if(month != "" && of_name != "" && NIC == "")
	{
		eel.month_office_view(year, month, of_name)(set_month_office_view)
	}
	else if(NIC != "" && of_name != "")
	{
		window.alert('You can\'t select both NIC and office name');
	}
	else if(NIC != "" && of_name != "" && month != "")
	{
		window.alert('You can\'t select both NIC and office name');
	}
}
function set_year_mul_view(result)
{
	if(result == "Not found")
	{
		window.alert('No records found in the specified year');
	}
	else if(result == "False")
	{
		window.alert('No records found in the specified year');
	}
	else
	{
		var x = document.createElement("TH");
		var t = document.createTextNode("NIC");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Office Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jan");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Feb");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Mar");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Apr");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("May");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jun");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jul");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Aug");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Sep");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Oct");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Nov");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Dec");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Total");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var i;
		for(i=0; i<result.length; i++)
		{
			var y = document.createElement("TR");
			y.setAttribute("id", i);
			document.getElementById("pay_view_table").appendChild(y);
			for (j=0; j<result[i].length; j++)
			{
				var z = document.createElement("TD");
				var t = document.createTextNode((result[i][j].toString()).replaceAll("*",","));
				z.appendChild(t);
				document.getElementById(i).appendChild(z);
			}
		}
		window.stop();
	}
}

function set_month_mul_view(result)
{
	if(result == "Not found")
	{
		window.alert('Check NIC number');
	}
	else if(result == "False")
	{
		window.alert('No records found in the specified year');
	}
	else
	{
		var x = document.createElement("TH");
		var t = document.createTextNode("NIC");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Office Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Amount");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var i;
		for(i=0; i<result.length; i++)
		{
			var y = document.createElement("TR");
			y.setAttribute("id", i);
			document.getElementById("pay_view_table").appendChild(y);
			for (j=0; j<result[i].length; j++)
			{
				var z = document.createElement("TD");
				var t = document.createTextNode((result[i][j].toString()).replaceAll("*", ","));
				z.appendChild(t);
				document.getElementById(i).appendChild(z);
			}
		}
		window.stop()
	}
}

function reset_func()
{
	window.open("sin_per_view.html", "_self");
}

function set_year_sin_view(result)
{
	if(result == "Not found")
	{
		window.alert('Check NIC number');
	}
	else if(result == "False")
	{
		window.alert('No records found in the specified year');
	}
	else
	{
		var x = document.createElement("TH");
		var t = document.createTextNode("NIC");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Office Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jan");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Feb");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Mar");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Apr");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("May");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jun");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jul");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Aug");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Sep");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Oct");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Nov");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Dec");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Total");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var i;
		var y = document.createElement("TR");
		y.setAttribute("id", "j");
		document.getElementById("pay_view_table").appendChild(y);
		for(i=0; i<result.length; i++)
		{
			var z = document.createElement("TD");
			var t = document.createTextNode((result[i].toString()).replaceAll("*", ","));
			z.appendChild(t);
			document.getElementById("j").appendChild(z);
		}
		window.stop()
	}
}

function set_month_sin_view(result)
{
	if(result == "Not found")
	{
		window.alert('Check NIC number');
	}
	else if(result == "False")
	{
		window.alert('No records found in the specified year');
	}
	else
	{
			
		var x = document.createElement("TH");
		var t = document.createTextNode("Amount");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		var i;
		for(i=0; i<result.length; i++)
		{
			var y = document.createElement("TR");
			y.setAttribute("id", i);
			document.getElementById("pay_view_table").appendChild(y);
			
			var z = document.createElement("TD");
			var t = document.createTextNode(result[i]);
			z.appendChild(t);
			document.getElementById(i).appendChild(z);
		}
		window.stop()
	}
}

function set_year_office_view(result)
{
	if(result == "Not found")
	{
		window.alert('No records found in the specified year');
	}
	else if(result == "False")
	{
		window.alert('No records found in the specified year');
	}
	else
	{
		var x = document.createElement("TH");
		var t = document.createTextNode("NIC");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Office Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jan");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Feb");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Mar");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Apr");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("May");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jun");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Jul");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Aug");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Sep");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Oct");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Nov");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Dec");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Total");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var i;
		for(i=0; i<result.length; i++)
		{
			var y = document.createElement("TR");
			y.setAttribute("id", i);
			document.getElementById("pay_view_table").appendChild(y);
			for (j=0; j<result[i].length; j++)
			{
				var z = document.createElement("TD");
				var t = document.createTextNode((result[i][j].toString()).replaceAll("*",","));
				z.appendChild(t);
				document.getElementById(i).appendChild(z);
			}
		}
		window.stop();
	}
}

function set_month_office_view(result)
{
	if(result == "Not found")
	{
		window.alert('Check NIC number');
	}
	else if(result == "False")
	{
		window.alert('No records found in the specified year');
	}
	else
	{
		var x = document.createElement("TH");
		var t = document.createTextNode("NIC");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Office Name");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var x = document.createElement("TH");
		var t = document.createTextNode("Amount");
		x.appendChild(t);
		document.getElementById("myTr").appendChild(x);
		
		var i;
		for(i=0; i<result.length; i++)
		{
			var y = document.createElement("TR");
			y.setAttribute("id", i);
			document.getElementById("pay_view_table").appendChild(y);
			for (j=0; j<result[i].length; j++)
			{
				var z = document.createElement("TD");
				var t = document.createTextNode((result[i][j].toString()).replaceAll("*", ","));
				z.appendChild(t);
				document.getElementById(i).appendChild(z);
			}
		}
		window.stop()
	}
}

function id_func()
{
	var NIC = document.getElementById("NIC").value;
	NIC = NIC.toString();
	NIC = NIC.replaceAll(',','*');
	eel.create_id(NIC)(set_id_func);
}