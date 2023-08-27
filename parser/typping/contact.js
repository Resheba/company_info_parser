() => 
{
    let temp = $(".hide-contact-one")[0]; 
    if (temp) {
        return  $._data(temp, "events").click[0].handler.toString()
    } else { 
        return null 
    } 
}