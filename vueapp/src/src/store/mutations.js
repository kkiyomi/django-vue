export const SET_TVSHOWS = (state, tvshows) => {
  state.tvshows = tvshows
}

export const SET_TVSHOW_PAGINATION = (state, tvshows) => {
  state.tvshows_paginated = tvshows
}

export const SET_TVSHOW = (state, tvshow) => {
  state.tvshow = tvshow
}

export const SET_RELEASE = (state, releases) => {
  state.releases = releases
}

export const SET_TVSHOW_GENRES = (state, genres) => {
  state.genres = genres
}

export const UPDATE_READINGLIST = (state, info) => {
  if (state.selected !== info.selected) {
    state.serie_set.find(value => value.id === info.id).current_release_id = info.selected
  }
}

export const ACCOUNT_INFO = (state, account) => {
  state.account = account[0]
}

export const ACCOUNT_REGISTER = (state, data) => {
  state.token = data.token
}

export const ACCOUNT_LOGIN = (state, data) => {
  state.token = data.token
}

export const ACCOUNT_READINGLIST = (state, data) => {
  state.serie_set = data
}

export const ALREADY_LOGGED_IN = (state, token) => {
  state.token = token
}

export const ACCOUNT_LOGOUT = (state) => {
  state.token = null
  state.account = null
  state.serie_set = []
}

export const GLOBAL_KEY = (state) => {
  state.globalKey += 1
}
