let count;

function sumarLikes()
{
    count = parseInt(document.getElementById('Likes').innerHTML);
    count++;
    document.getElementById('Likes').innerHTML=count;
    alert(" +1 Like :)");

}

function sumarLikes2(elemento)
{
    count = parseInt(document.getElementById(elemento).innerHTML);
    count++;
    document.getElementById(elemento).innerHTML=count;
    alert(" +1 Like :)");

}

// Giovanna Mella