document.addEventListener('DOMContentLoaded', () => {
    // var username = "{{ user.username }}";
    var date=''
alert(username);
	
$( "#datepicker" ).datepicker( "setDate", new Date() );

$("#datepicker" ).datepicker({
    onSelect: function(dateText) {
        console.log("Selected date: " + dateText + "; input's current value: " + this.value);
    }
})
.on("change", function() {
    
    loadorder(this.value);
});


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
loadorder = (date) => {
    var organizeddate= date.toString().substring(6,10)
    organizeddate+='-'+date.toString().substring(0,2)
    organizeddate+='-'+date.toString().substring(3,5)
    console.log(organizeddate)
    const loadorderrequest = new XMLHttpRequest();
    loadorderrequest.open('POST', 'getDS')
    loadorderrequest.onload = () => {
        const loaddata = JSON.parse(loadorderrequest.responseText);
        document.querySelector('#bodycontainer').innerHTML=''
        for (i = 0; i < loaddata['alldata'].length; i++) {

            const temptextchar=document.createElement('dir');
            for (var key in loaddata['alldata'][i]) {
                if (loaddata['alldata'][i].hasOwnProperty(key)) {
                    console.log(key + " ===" + loaddata['alldata'][i][key]);
                    temptextchar.innerHTML+=key + " : " + loaddata['alldata'][i][key]+'<br>'
                }}

            document.querySelector('#bodycontainer').appendChild(temptextchar);
        }

    }
    var csrftoken = getCookie('csrftoken');
    loadorderrequest.setRequestHeader('X-CSRFToken',csrftoken);
    const data= new FormData();
    data.append('drivername',username);
    data.append('date',organizeddate)
    loadorderrequest.send(data);

}
var date1 =  new Date()
loadorder($.datepicker.formatDate("mm-dd-yy", date1));
})