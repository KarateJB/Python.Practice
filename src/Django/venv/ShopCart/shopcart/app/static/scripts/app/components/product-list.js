var prodapp = new Vue({
    el: '#prodapp',
    data: {
    },
    methods: {
        confirmRemove: function (id, title) {
            var refs = this.$refs;

            swal({
                title: 'Are you sure?',
                text: `\"${title}\" will be removed!`,
                type: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Yes, delete it!',
                cancelButtonText: 'No',
                confirmButtonClass: 'btn btn-success',
                cancelButtonClass: 'btn btn-danger',
            }).then(function () {
                let form = "removeForm" + id.toString();
                console.log('form=' + form)
                refs[form].submit(); //Submit

            }, function (dismiss) {

            })
        }
    }
})