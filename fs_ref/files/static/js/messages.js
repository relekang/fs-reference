var closeBtn='<button class="close" data-dismiss="alert">×</button>';
function addError(message){addMessage(message,"alert-error");}
function addSuccess(message){addMessage(message,"alert-success");}
function addInfo(message){addMessage(message,"alert-info");}
function addMessage(message,type){$("#alert").html("<div></div>");var alert=$("#alert").children("div");alert.addClass("alert");if(type!="")alert.addClass(type);alert.html(closeBtn+"\n"+message);}

function addModalError(message){addModalMessage(message,"alert-error");}
function addModalSuccess(message){addModalMessage(message,"alert-success");}
function addModalInfo(message){addModalMessage(message,"alert-info");}
function addModalMessage(message,type){$("#modal-alert").html("<div></div>");var alert=$("#modal-alert").children("div");alert.addClass("alert");if(type!="")alert.addClass(type);alert.html(closeBtn+"\n"+message);}
