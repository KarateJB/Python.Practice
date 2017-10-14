var app = new Vue({
    el: '#app',
    data: {
        isShowMenu : false,
        homeTitle : "Welcome to Django!"
    },
    methods: {
        toggleMenu: function () {
            if (this.isShowMenu === false){
                this.isShowMenu = true;
            }
            else {
                this.isShowMenu = false;
                
            }
        }
    }
})