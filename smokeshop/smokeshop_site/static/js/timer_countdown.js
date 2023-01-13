function updateTime() {
    $.ajax({
        url: "/get_remaining_time",
        success: function(data) {
            $("#ad-p-2").text(data.time_left);
        }
    });
    setTimeout(updateTime, 1000);
}
updateTime();