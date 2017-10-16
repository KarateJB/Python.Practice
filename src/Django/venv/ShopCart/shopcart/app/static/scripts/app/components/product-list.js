var prodapp = new Vue({
    el: '#prodapp',
    data: {
    },
    methods: {
        confirmRemove: function (title) {
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

                refs.removeForm.submit(); //Submit

            }, function (dismiss) {

            })
        }
    }
})