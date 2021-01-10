<template>
  <v-container fluid>

    <v-row>
      <v-img contain :src="require('@/assets/bg.png')" :style="{'filter': $vuetify.theme.dark ? 'invert(1)': 'invert(0)'}">
        <template v-slot:placeholder>
          <v-skeleton-loader
          type="image"
          class="fill-height ma-0"
          align="center"
          justify="center"
          ></v-skeleton-loader>
      </template>
      </v-img>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" class="text-center text--secondary">
        <h2>Our Features</h2>
        <p><b>Our 3 Primary Features -</b></p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="i in Features" :key="i.id" align="center">
          <v-img
            width="125px"
            :src="i.img"
          >
            <template v-slot:placeholder>
              <v-skeleton-loader
              type="image"
              class="fill-height ma-0"
              ></v-skeleton-loader>
            </template>
          </v-img>
          <v-card-title class="justify-center">{{i.title}}</v-card-title>
          <v-card-text class="text-center">
            {{ i.body }}
          </v-card-text>
      </v-col>
    </v-row>

    
    <v-row justify="center">
      <v-col cols="12" class="text-center text--secondary">
        <h2>Our Features</h2>
        <p><b>We have a Simple Features</b></p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="i in Process" :key="i.id" align="center">
          <v-img
            width="125px"
            :src="i.img"
          >
            <template v-slot:placeholder>
              <v-skeleton-loader
              type="image"
              class="fill-height ma-0"
              ></v-skeleton-loader>
            </template>
          </v-img>
          <v-card-title class="justify-center">{{i.title}}</v-card-title>
          <v-card-text class="text-center">
            {{ i.body }}
          </v-card-text>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
// @ is an alias to /src
// import { mapGetters } from 'vuex'

export default {
  name: 'Home',
  data(){
    return {
      Features: [
        {
          id:1,
          img: require("@/assets/Images/responsive.svg"),
          title: 'Simple & Easy to Use',
          body: "The ePustakalay is simple, user-friendly, and can be easily integrated with your existing system. The ePustakalay benefits provide online and offline storage, automated backups, and easy upgrades to simplify and enhance the learning process."
        },
        {
          id:2,
          img: require("@/assets/Images/page_find.svg"),
          title: 'Search Books',
          body: "The ePustakalay provides mobile access to search the library catalog, schedules, books and resources from anywhere, at any given time via smartphones and tablets etc."
        },
        {
          id:3,
          img: require("@/assets/Images/map.svg"),
          title: 'Cost-effective',
          body: "Embracing sophisticated technologies is cost-effective and a viable choice for education institutions. Using cloud, mobile and digital libraries eliminates paper-based processes and maintenance overheads, improves productivity, reduces operation costs and saves time."
        }
      ],
      Process:[
        {
          id:1,
          img: require("@/assets/Images/privacy.svg"),
          title: 'Record Maintenance',
          body: "All records related to the book issued and return deadline can managed by the authorised personnel. The system also allows to record the fine received from the student in the same platform, which eases the work of reporting for the Library department."
        },
        {
          id:2,
          img: require("@/assets/Images/secure_server.svg"),
          title: 'Secure and Reliable',
          body: "The paper based process might incur data loss, however in case of Library Management System, it is much secure and reliable. Only the authorised personnel can login to the system and use it."
        },
        {
          id:3,
          img: require("@/assets/Images/maintainable.svg"),
          title: 'Fully Customizable',
          body: "The ePustakalay automation system is fully customizable and adaptable to the needs of educational institutions to provide fast, reliable data."
        }
      ]
    }
  }
}
</script>