<template>
    <div>
        <h1 style="color:red">Http404 Path: {{ $route.path }} Not Valid</h1>
    </div>
</template>

<script>
export default {
    name: 'Http404',
    created(){
        document.title = "Not Find " + this.$router.history.current.path
        console.log(this.$router);
    },
}
</script>
