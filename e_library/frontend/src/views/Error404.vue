<template>
    <v-container class="yellow">
        <v-row class="blue">
            <v-col class="white black--text">
                current this.$vuetify.breakpoint.width {{ $vuetify.breakpoint.width }} <br>
                xs  	&lt; 600px <br>
                sm	600px > &lt; 960px <br>
                md	960px > &lt; 1264px* <br>
                lg 1264px > &lt; 1904px* <br>
                xl	> 1904px* <br>
            </v-col>
        </v-row>
        <v-row class="green">
            <v-col cols="12" sm="6" md="4" xl="12" class="pink">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat dignissimos repellat, dolores blanditiis et eaque molestiae. Minus illum recusandae fuga molestiae, eligendi perspiciatis, a laudantium exercitationem aliquid iste et consequatur.
            </v-col>
            <v-col cols="12" sm="6" md="4" xl="12" class="red">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed provident reiciendis qui repellat laudantium maiores harum voluptates delectus quae. Eaque vel ipsum ipsa numquam esse repellat amet illum quibusdam ducimus.
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name:'Error404',
    created:function(){
        console.log(this.$vuetify.breakpoint.width)
    }
}
</script>