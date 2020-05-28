document.addEventListener('DOMContentLoaded', () => {
    var driverlist = []
    var driverindex = 0
    var startdate;
    var pk =NaN;
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    loadorder = () => {
        const loadorderrequest = new XMLHttpRequest();
        loadorderrequest.open('GET', 'getO')
        loadorderrequest.onload = () => {
            const loaddata = JSON.parse(loadorderrequest.responseText);
            tempchildlist = []
            for (var key in loaddata) {
                if (loaddata.hasOwnProperty(key)) {
                    console.log(key + " ===" + loaddata[key]);
                    tempchild = document.createElement('li')
                    tempchild.innerHTML = key + " : " + loaddata[key]
                    tempchildlist.push(tempchild)
                    if (key == 'start_day') {


                        startdate = loaddata[key]
                    }

                    if (key == 'pk') {


                        pk = loaddata[key]
                        const myeditlikk = document.createElement('a');
                        myeditlikk.setAttribute('href','edit/'+pk)
                        myeditlikk.setAttribute('target',"_blank")
                        myeditlikk.innerHTML='edit this order'
                        tempchildlist.push(myeditlikk)
                    }


                }
            }
            document.querySelector('#headcontainer').innerHTML = '';
            templist = document.createElement('ul')
            for (i = 0; i < tempchildlist.length; i++) { templist.appendChild(tempchildlist[i]); }
            document.querySelector('#headcontainer').appendChild(templist);

        }
        loadorderrequest.send();

    }
    loaddriverlist = () => {
        loaddriverlistrequest = new XMLHttpRequest();
        loaddriverlistrequest.open('GET', "getD");

        loaddriverlistrequest.onload = () => {
            document.querySelector('#driversekect').innerHTML = ''
            const loaddata = JSON.parse(loaddriverlistrequest.responseText);
            driverlist = []
            for (i = 0; i < loaddata['namelist'].length; i++) {
                driverlist.push(loaddata['namelist'][i])
                console.log(loaddata['namelist'][i])
                tempchild = document.createElement('option')
                tempchild.value = loaddata['namelist'][i];
                tempchild.innerHTML = loaddata['namelist'][i]
                document.querySelector('#driversekect').appendChild(tempchild)
            }
         loaddriverscadule(document.querySelector('#driversekect').value);
        
            document.querySelector('#driversekect').onchange = () => { loaddriverscadule(document.querySelector('#driversekect').value) };

        }
        loaddriverlistrequest.send();



    }
    loaddriverscadule = function (drivername) {

        
        loaddriverscadulerequest = new XMLHttpRequest();
        
        
   
        loaddriverscadulerequest.open('POST', 'getDS');var csrftoken = getCookie('csrftoken');
        loaddriverscadulerequest.setRequestHeader('X-CSRFToken',csrftoken);
        
        loaddriverscadulerequest.onload=()=>{
            const loaddata = JSON.parse(loaddriverscadulerequest.responseText);
            document.querySelector('#bodycontainer').innerHTML=''
            for (i = 0; i < loaddata['alldata'].length; i++) {

                const temptextchar=document.createElement('dir');
                for (var key in loaddata['alldata'][i]) {
                    if (loaddata['alldata'][i].hasOwnProperty(key)) {
                        console.log(key + " ===" + loaddata['alldata'][i][key]);
                        temptextchar.innerHTML+=key + " ===" + loaddata['alldata'][i][key]+'<br>'
                    }}

                document.querySelector('#bodycontainer').appendChild(temptextchar);
            }


        }
        const data= new FormData();
        data.append('drivername',drivername);
        data.append('date',startdate);
     
        loaddriverscadulerequest.send(data);




    }

    if (confirm('sendrequest')) {
        loadorder();
        loaddriverlist()
    }





})