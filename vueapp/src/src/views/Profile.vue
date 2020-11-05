<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row align="center" justify="center">
          <v-col>
            <v-card class="mx-auto" tile v-if="account">
              <v-img height="200" src=""></v-img>
              <div class="mx-4" style="position:absolute; top: 160px">
              <v-row>
                <v-list-item>
                  <v-list-item-avatar size="110">
                    <img src="https://www.w3schools.com/howto/img_avatar.png" alt="John">
                  </v-list-item-avatar>
                  <v-list-item-content class="mt-2">
                    <v-list-item-title class="title mt-2">
                      {{ account.username }}
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      Member
                    </v-list-item-subtitle>
                  </v-list-item-content>
                  <div class="mx-2">
                    Joined: {{ dateFormated }}
                  </div>
                  <div class="mx-2">
                    <AddTvshow></AddTvshow>
                  </div>
                </v-list-item>
              </v-row>
              <v-row class="mt-4">
                <AddTvshow></AddTvshow>
              </v-row>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
import AddTvshow from '../components/Profile/AddTvshow.vue'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Profile',

  components: {
    AddTvshow
  },

  data () {
    return {
      dialogAddtv: false,
    }
  },
  computed: {
    ...mapState(['account']),
    dateFormated () {
      return this.account.date_joined.split('T')[0]
    }
  },
  methods: {
    ...mapActions(['getAccountInfo', 'getTVShowGenres']),
  },
  async created () {
    await this.getTVShowGenres()
  }
}

</script>
