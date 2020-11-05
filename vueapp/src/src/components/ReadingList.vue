<template>
  <div>
  <div v-if="account">
    <v-card
      class="mx-auto"
      width="700"
      outlined
      v-if="serie_set"
      :key="globalKey"
    >
      <v-card-title v-if="account.readinglist === null">
        <v-btn class="ml-4" @click="AddList">
          activate Reading List
        </v-btn>
      </v-card-title>
      <v-card-title v-else>
        Reading List
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        v-if="account.readinglist !== null"
        dense
        :headers="headers"
        :items="serie_set"
        :search="search"
        v-model="selected"
        item-key="tvshow.id"
        show-select
        class="elevation-1"
      >
        <template #item.tvshow="{item}">
          <router-link class="red-link"
            :to="{ name: 'TvshowDetail', params: { slug: item.tvshow.slug, id:item.tvshow.id }}">{{ item.tvshow.title }}
          </router-link>
        </template>
        <template #item.release="{item}">
          <a :href="item.release.link" class="red-link" target="_blank">
            {{ item.release.number }}
          </a>
        </template>
        <template #item.latest="{item}">
          <a :href="item.tvshow.latest.link" class="red-link" target="_blank">
          g {{item.tvshow.latest.number}}
          </a>
        </template>
        <template slot="footer">
            <v-btn style="position: absolute; left: 10px; bottom: 10px;"
              elevation="2"
              color="error"
              v-if="selected.length !== 0"
              @click="RemoveSerieFromReadingList"
              text
            >
              Remove
            </v-btn>
            <RemoveSerieDialog v-if="globalKey < 0" :selected="selected"></RemoveSerieDialog>
        </template>
      </v-data-table>
    </v-card>
  </div>
  <div v-else>
    log in first
  </div>
  </div>
</template>

<script>
import RemoveSerieDialog from './RemoveSerieDialog.vue'
import { mapState, mapActions } from 'vuex'
export default {
  name: 'ReadingList',

  components: {
    RemoveSerieDialog,
  },

  data () {
    return {
      dialog: false,
      selectedRelease: 2,
      selected: [],
      search: '',
      headers: [
        { text: 'Series', value: 'tvshow' },
        { text: 'My Status', value: 'release', width: '150' },
        { text: 'Latest Release', value: 'latest', width: '150' },
        { text: 'Date', value: 'date_added' },
      ],
    }
  },
  async mounted () {
    await this.AccountReadinglist(this.account.id)
    this.fixList()
  },
  computed: {
    ...mapState(['serie_set', 'account', 'globalKey']),
  },
  methods: {
    ...mapActions(['AccountReadinglist', 'getAccountInfo', 'AddReadinglist', 'DeleteSerieFromReadingList', 'gkey']),
    async RemoveSerieFromReadingList () {
      this.dialog = !this.dialog
      for (var i = 0; i <= this.selected.length - 1; i++) {
        await this.DeleteSerieFromReadingList(this.selected[i].id)
      }
      this.selected = []
      await this.AccountReadinglist(this.account.id)
      this.gkey()
    },
    async AddList () {
      await this.AddReadinglist()
      await this.getAccountInfo()
      await this.AccountReadinglist(this.account.id)
      this.gkey()
    },
    fixList () {
      const newArray = []
      for (var i = 0; i < this.serie_set.length; i++) {
        const fd = {}
        fd.append('id', this.serie_set[i].id)
        fd.append('cur_release_id', this.serie_set[i].current_release_id)
        fd.append('tvshow_id', this.serie_set[i].tvshow.id)
        fd.append('tvshow_title', this.serie_set[i].tvshow.title)
        fd.append('tvshow_slug', this.serie_set[i].tvshow.slug)
        fd.append('tvshow_latest_id', this.serie_set[i].tvshow.latest.id)
        fd.append('tvshow_latest_number', this.serie_set[i].tvshow.latest.number)
        fd.append('tvshow_latest_link', this.serie_set[i].tvshow.latest.link)
        fd.append('tvshow_latest_date_added', this.serie_set[i].tvshow.latest.date_added)
        fd.append('tvshow_release_id', this.serie_set[i].release.id)
        fd.append('tvshow_release_number', this.serie_set[i].release.number)
        fd.append('tvshow_release_link', this.serie_set[i].release.link)
        fd.append('tvshow_release_date_added', this.serie_set[i].release.date_added)
        newArray.push(fd)
      }
      console.log(newArray)
    }
  }
}
</script>
