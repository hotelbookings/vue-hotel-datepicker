<template>
  <div
    class="vhd__datepicker__wrapper"
    :class="{
      'vhd__datepicker__wrapper--grid': gridStyle,
      'vhd__datepicker__wrapper--booking': bookings.length > 0,
      vhd__datepicker__fullview: alwaysVisible,
      'vhd__datepicker__wrapper--inCustomPeriod': isInCustomPeriod,
    }"
    :ref="`DatePicker-${hash}`"
    v-if="value"
  >
    <div class="vhd__datepicker__dummy-wrapper" :class="{ 'vhd__datepicker__dummy-wrapper--is-active': isOpen }">
      <div class="vhd__datepicker__input__svg">
        <svg
          aria-hidden="true"
          focusable="false"
          data-prefix="fal"
          data-icon="calendar-alt"
          role="img"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 448 512"
          class="svg-inline--fa fa-calendar-alt fa-w-14"
        >
          <path
            d="M400 64h-48V12c0-6.6-5.4-12-12-12h-8c-6.6 0-12 5.4-12 12v52H128V12c0-6.6-5.4-12-12-12h-8c-6.6 0-12 5.4-12 12v52H48C21.5 64 0 85.5 0 112v352c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V112c0-26.5-21.5-48-48-48zM48 96h352c8.8 0 16 7.2 16 16v48H32v-48c0-8.8 7.2-16 16-16zm352 384H48c-8.8 0-16-7.2-16-16V192h384v272c0 8.8-7.2 16-16 16zM148 320h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm96 0h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm96 0h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm-96 96h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm-96 0h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm192 0h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12z"
            class=""
            fill="var(--primary_color)"
          ></path>
        </svg>
      </div>
      <date-input
        :i18n="i18n"
        :input-date="formatDate(checkIn)"
        input-date-type="check-in"
        :is-open="isOpen"
        :toggle-datepicker="toggleDatepicker"
        :single-day-selection="singleDaySelection"
      />
      <div class="vhd__datepicker__input__svg vhd__datepicker__input__svg--separator">
        <svg
          aria-hidden="true"
          focusable="false"
          data-prefix="fal"
          data-icon="chevron-right"
          role="img"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 256 512"
          class="svg-inline--fa fa-chevron-right fa-w-8"
          style=""
        >
          <path
            fill="currentColor"
            d="M17.525 36.465l-7.071 7.07c-4.686 4.686-4.686 12.284 0 16.971L205.947 256 10.454 451.494c-4.686 4.686-4.686 12.284 0 16.971l7.071 7.07c4.686 4.686 12.284 4.686 16.97 0l211.051-211.05c4.686-4.686 4.686-12.284 0-16.971L34.495 36.465c-4.686-4.687-12.284-4.687-16.97 0z"
            class=""
            style=""
          ></path>
        </svg>
      </div>
      <date-input
        v-if="!singleDaySelection"
        :i18n="i18n"
        :input-date="formatDate(checkOut)"
        input-date-type="check-out"
        :is-open="isOpen"
        :toggle-datepicker="toggleDatepicker"
        :single-day-selection="singleDaySelection"
      />
      <div class="vhd__datepicker__input__svg vhd__datepicker__input__svg--clear-button">
        <div
          class="vhd__datepicker__clear-button"
          tabindex="0"
          @click="clearSelection"
          v-show="showClearSelectionButton"
        >
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fal"
            data-icon="times"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 320 512"
            class="svg-inline--fa fa-times fa-w-10"
          >
            <path
              fill="currentColor"
              d="M193.94 256L296.5 153.44l21.15-21.15c3.12-3.12 3.12-8.19 0-11.31l-22.63-22.63c-3.12-3.12-8.19-3.12-11.31 0L160 222.06 36.29 98.34c-3.12-3.12-8.19-3.12-11.31 0L2.34 120.97c-3.12 3.12-3.12 8.19 0 11.31L126.06 256 2.34 379.71c-3.12 3.12-3.12 8.19 0 11.31l22.63 22.63c3.12 3.12 8.19 3.12 11.31 0L160 289.94 262.56 392.5l21.15 21.15c3.12 3.12 8.19 3.12 11.31 0l22.63-22.63c3.12-3.12 3.12-8.19 0-11.31L193.94 256z"
              class=""
            ></path>
          </svg>
        </div>
      </div>
    </div>
    <div
      class="vhd__datepicker"
      :class="{
        'vhd__datepicker--open': isOpen && !alwaysVisible,
        'vhd__datepicker--closed': !isOpen && !alwaysVisible,
        'vhd__datepicker--right': positionRight,
      }"
    >
      <div class="vhd__hide-on-desktop">
        <div
          v-if="isOpen"
          class="vhd__datepicker__dummy-wrapper vhd__datepicker__dummy-wrapper--no-border"
          :class="{ 'vhd__datepicker__dummy-wrapper--is-active': isOpen }"
          @click="toggleDatepicker"
        >
          <div class="vhd__datepicker__input__svg">
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fal"
              data-icon="calendar-alt"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 448 512"
              class="svg-inline--fa fa-calendar-alt fa-w-14"
            >
              <path
                d="M400 64h-48V12c0-6.6-5.4-12-12-12h-8c-6.6 0-12 5.4-12 12v52H128V12c0-6.6-5.4-12-12-12h-8c-6.6 0-12 5.4-12 12v52H48C21.5 64 0 85.5 0 112v352c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V112c0-26.5-21.5-48-48-48zM48 96h352c8.8 0 16 7.2 16 16v48H32v-48c0-8.8 7.2-16 16-16zm352 384H48c-8.8 0-16-7.2-16-16V192h384v272c0 8.8-7.2 16-16 16zM148 320h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm96 0h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm96 0h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm-96 96h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm-96 0h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm192 0h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12z"
                class=""
                fill="var(--primary_color)"
              ></path>
            </svg>
          </div>
          <div
            class="vhd__datepicker__input"
            tabindex="0"
            :class="{
              'vhd__datepicker__dummy-input--is-active': isOpen && checkIn == null,
            }"
            type="button"
          >
            {{ `${checkIn ? formatDate(checkIn) : i18n['check-in']}` }}
          </div>
          <div class="vhd__datepicker__input__svg vhd__datepicker__input__svg--separator">
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fal"
              data-icon="chevron-right"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 256 512"
              class="svg-inline--fa fa-chevron-right fa-w-8"
              style=""
            >
              <path
                fill="currentColor"
                d="M17.525 36.465l-7.071 7.07c-4.686 4.686-4.686 12.284 0 16.971L205.947 256 10.454 451.494c-4.686 4.686-4.686 12.284 0 16.971l7.071 7.07c4.686 4.686 12.284 4.686 16.97 0l211.051-211.05c4.686-4.686 4.686-12.284 0-16.971L34.495 36.465c-4.686-4.687-12.284-4.687-16.97 0z"
                class=""
                style=""
              ></path>
            </svg>
          </div>
          <div
            class="vhd__datepicker__input"
            tabindex="0"
            :class="{
              'vhd__datepicker__dummy-input--is-active': isOpen && checkOut == null && checkIn !== null,
            }"
            type="button"
          >
            {{ `${checkOut ? formatDate(checkOut) : i18n['check-out']}` }}
          </div>
          <div class="vhd__datepicker__close-button vhd__hide-on-desktop" v-if="isOpen" @click="closeMobileDatepicker">
            <div
              class="vhd__datepicker__clear-button"
              tabindex="0"
              @click="clearSelection"
              v-show="showClearSelectionButton"
            >
              <svg
                aria-hidden="true"
                focusable="false"
                data-prefix="fal"
                data-icon="times"
                role="img"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 320 512"
                class="svg-inline--fa fa-times fa-w-10"
              >
                <path
                  fill="currentColor"
                  d="M193.94 256L296.5 153.44l21.15-21.15c3.12-3.12 3.12-8.19 0-11.31l-22.63-22.63c-3.12-3.12-8.19-3.12-11.31 0L160 222.06 36.29 98.34c-3.12-3.12-8.19-3.12-11.31 0L2.34 120.97c-3.12 3.12-3.12 8.19 0 11.31L126.06 256 2.34 379.71c-3.12 3.12-3.12 8.19 0 11.31l22.63 22.63c3.12 3.12 8.19 3.12 11.31 0L160 289.94 262.56 392.5l21.15 21.15c3.12 3.12 8.19 3.12 11.31 0l22.63-22.63c3.12-3.12 3.12-8.19 0-11.31L193.94 256z"
                  class=""
                ></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <div v-if="isOpen || alwaysVisible" class="vhd__datepicker__inner">
        <template v-show="isInCustomPeriod">
          <slot name="monthHeaderSlot" />
        </template>
        <template v-if="!isDesktop" v-show="isInCustomPeriod">
          <slot name="monthFooterSlot" />
        </template>
        <div
          :class="{
            vhd__datepicker__header: isDesktop,
            'vhd__datepicker__header-mobile': !isDesktop,
          }"
        >
          <button
            type="button"
            class="vhd__datepicker__month-button vhd__datepicker__month-button--prev"
            @click="renderPreviousMonth"
            @keyup.enter.stop.prevent="renderPreviousMonth"
            :tabindex="isOpen ? 0 : -1"
            :disabled="activeMonthIndex === 0"
          >
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fal"
              data-icon="chevron-left"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 256 512"
              class="svg-inline--fa fa-chevron-left fa-w-8"
            >
              <path
                d="M238.475 475.535l7.071-7.07c4.686-4.686 4.686-12.284 0-16.971L50.053 256 245.546 60.506c4.686-4.686 4.686-12.284 0-16.971l-7.071-7.07c-4.686-4.686-12.284-4.686-16.97 0L10.454 247.515c-4.686 4.686-4.686 12.284 0 16.971l211.051 211.05c4.686 4.686 12.284 4.686 16.97-.001z"
                class=""
                fill="var(--primary_color)"
              ></path>
            </svg>
          </button>
          <button
            type="button"
            class="vhd__datepicker__month-button vhd__datepicker__month-button--next"
            @click="renderNextMonth"
            @keyup.enter.stop.prevent="renderNextMonth"
            :disabled="isPreventedMaxMonth"
            :tabindex="isOpen ? 0 : -1"
          >
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fal"
              data-icon="chevron-right"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 256 512"
              class="svg-inline--fa fa-chevron-right fa-w-8"
            >
              <path
                d="M17.525 36.465l-7.071 7.07c-4.686 4.686-4.686 12.284 0 16.971L205.947 256 10.454 451.494c-4.686 4.686-4.686 12.284 0 16.971l7.071 7.07c4.686 4.686 12.284 4.686 16.97 0l211.051-211.05c4.686-4.686 4.686-12.284 0-16.971L34.495 36.465c-4.686-4.687-12.284-4.687-16.97 0z"
                class=""
                fill="var(--primary_color)"
              ></path>
            </svg>
          </button>
        </div>
        <div
          v-if="isDesktop || alwaysVisible"
          class="vhd__datepicker__months"
          :class="{ 'vhd__datepicker__months--full': showSingleMonth }"
        >
          <Month
            v-for="(month, monthIndex) in paginateMonths"
            :key="`${datepickerMonthKey}-${monthIndex}-desktop`"
            ref="datepickerMonth"
            :month="month"
            :dayKey="datepickerDayKey"
            :weekKey="datepickerWeekKey"
            :isDesktop="isDesktop"
            :firstDayOfWeek="firstDayOfWeek"
            :showYear="showYear"
            :yearBeforeMonth="yearBeforeMonth"
            :activeMonthIndex="activeMonthIndex"
            :bookings="sortBookings"
            :checkIn="checkIn"
            :checkIncheckOutHalfDay="checkIncheckOutHalfDay"
            :checkInPeriod="checkInPeriod"
            :checkOut="checkOut"
            :customPeriod="customPeriod"
            :disableCheckoutOnCheckin="disableCheckoutOnCheckin"
            :duplicateBookingDates="duplicateBookingDates"
            :hoveringDate="hoveringDate"
            :hoveringPeriod="hoveringPeriod"
            :i18n="i18n"
            :isOpen="isOpen"
            :minNightCount="minNightCount"
            :nextDisabledDate="nextDisabledDate"
            :nextPeriodDisableDates="nextPeriodDisableDates"
            :options="dayOptions"
            :priceSymbol="priceSymbol"
            :screenSize="screenSize"
            :showCustomTooltip="showCustomTooltip"
            :showPrice="showPrice"
            :showWeekNumbers="showWeekNumbers"
            :disabledDates="disabledDates"
            :periodDates="periodDates"
            :sortedDisabledDates="sortedDisabledDates"
            :sortedPeriodDates="sortedPeriodDates"
            :tooltipMessage="customTooltipMessage"
            @clear-selection="clearSelection"
            @booking-clicked="handleBookingClicked"
            @day-clicked="handleDayClick"
            @enter-day="enterDay"
            @enter-month="enterMonth"
          />
        </div>
        <div
          v-if="!isDesktop && isOpen && !alwaysVisible"
          :class="['vhd__datepicker__months-wrapper', { 'vhd__show-tooltip': showCustomTooltip && hoveringTooltip }]"
        >
          <div class="vhd__datepicker__tooltip--mobile" v-if="hoveringTooltip">
            <template v-if="customTooltipMessage">
              {{ cleanString(customTooltipMessage) }}
            </template>
          </div>
          <div class="vhd__datepicker__months" ref="swiperWrapper">
            <Month
              v-for="(month, monthIndex) in paginateMonths"
              :key="`${datepickerMonthKey}-${monthIndex}-desktop`"
              ref="datepickerMonth"
              :month="month"
              :dayKey="datepickerDayKey"
              :weekKey="datepickerWeekKey"
              :isDesktop="isDesktop"
              :firstDayOfWeek="firstDayOfWeek"
              :showYear="showYear"
              :yearBeforeMonth="yearBeforeMonth"
              :activeMonthIndex="activeMonthIndex"
              :bookings="sortBookings"
              :checkIn="checkIn"
              :checkIncheckOutHalfDay="checkIncheckOutHalfDay"
              :checkInPeriod="checkInPeriod"
              :checkOut="checkOut"
              :customPeriod="customPeriod"
              :disableCheckoutOnCheckin="disableCheckoutOnCheckin"
              :duplicateBookingDates="duplicateBookingDates"
              :hoveringDate="hoveringDate"
              :hoveringPeriod="hoveringPeriod"
              :i18n="i18n"
              :isOpen="isOpen"
              :minNightCount="minNightCount"
              :nextDisabledDate="nextDisabledDate"
              :nextPeriodDisableDates="nextPeriodDisableDates"
              :options="dayOptions"
              :priceSymbol="priceSymbol"
              :screenSize="screenSize"
              :showCustomTooltip="false"
              :showPrice="showPrice"
              :sortedDisabledDates="sortedDisabledDates"
              :sortedPeriodDates="sortedPeriodDates"
              :tooltipMessage="customTooltipMessage"
              @clear-selection="clearSelection"
              @booking-clicked="handleBookingClicked"
              @day-clicked="handleDayClick"
              @enter-day="enterDay"
              @enter-month="enterMonth"
            />
          </div>
        </div>
        <template v-if="isDesktop">
          <template v-show="isInCustomPeriod">
            <slot name="monthFooterSlot" />
          </template>
        </template>
      </div>
      <slot name="content" />
    </div>
  </div>
</template>

<script>
import throttle from 'lodash.throttle'
import fecha from 'fecha'

import Month from './components/Month.vue'
import DateInput from './components/DateInput.vue'
import Helpers from '../helpers'
import i18nDefaults from '../../public/i18n/en'

export default {
  name: 'HotelDatePicker',
  components: {
    Month,
    DateInput,
  },
  props: {
    alwaysVisible: {
      type: Boolean,
      default: false,
    },
    bookings: {
      type: Array,
      default() {
        return []
      },
    },
    closeDatepickerOnClickOutside: {
      type: Boolean,
      default: true,
    },
    customPeriod: {
      type: Array,
      default: () => [],
    },
    disableCheckoutOnCheckin: {
      type: Boolean,
      default: false,
    },
    disabledDates: {
      type: Array,
      default() {
        return []
      },
    },
    disabledDaysOfWeek: {
      type: Array,
      default() {
        return []
      },
    },
    disabledWeekDays: {
      type: Object,
      default() {
        return {}
      },
    },
    displayClearButton: {
      type: Boolean,
      default: true,
    },
    enableCheckout: {
      type: Boolean,
      default: false,
    },
    endDate: {
      type: [Date, String, Number],
      default: Infinity,
    },
    endingDateValue: {
      type: [Date, null],
      default: null,
    },
    firstDayOfWeek: {
      type: Number,
      default: 0,
    },
    format: {
      type: String,
      default: 'YYYY-MM-DD',
    },
    gridStyle: {
      type: Boolean,
      default: true,
    },
    halfDay: {
      type: Boolean,
      default: true,
    },
    hoveringTooltip: {
      default: true,
      type: [Boolean, Function],
    },
    i18n: {
      type: Object,
      default: () => i18nDefaults,
    },
    lastDateAvailable: {
      type: [Number, Date],
      default: Infinity,
    },
    maxNights: {
      type: [Number, null],
      default: null,
    },
    minNights: {
      type: Number,
      default: 1,
    },
    periodDates: {
      type: Array,
      default() {
        return []
      },
    },
    positionRight: {
      type: Boolean,
      default: false,
    },
    priceSymbol: {
      type: String,
      default: '',
    },
    showPrice: {
      type: Boolean,
      default: false,
    },
    showSingleMonth: {
      type: Boolean,
      default: false,
    },
    showYear: {
      type: Boolean,
      default: true,
    },
    showWeekNumbers: {
      type: Boolean,
      default: false,
    },
    showTooltipOnOneDay: {
      type: Boolean,
      default: true,
    },
    singleDaySelection: {
      type: Boolean,
      default: false,
    },
    startDate: {
      type: [Date, String],
      default() {
        return new Date()
      },
    },
    startingDateValue: {
      type: [Date, null],
      default: null,
    },
    tooltipMessage: {
      type: [String, null],
      default: null,
    },
    value: {
      type: Boolean,
      default: true,
    },
    yearBeforeMonth: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      activeMonthIndex: 0,
      checkIn: this.startingDateValue,
      checkIncheckOutHalfDay: {},
      checkInPeriod: {},
      checkOut: this.endingDateValue,
      hoveringPeriod: {},
      customTooltip: '',
      customTooltipHalfday: '',
      datepickerDayKey: 0,
      datepickerMonthKey: 0,
      datepickerWeekKey: 0,
      dynamicNightCounts: null,
      hash: Date.now(),
      hoveringDate: null,
      isTouchMove: false,
      months: [],
      nextDisabledDate: null,
      nextPeriodDisableDates: [],
      open: false,
      screenSize: null,
      showCustomTooltip: false,
      sortedDisabledDates: null,
      xDown: null,
      xUp: null,
      yDown: null,
      yUp: null,
    }
  },
  computed: {
    isOpen: {
      get() {
        return this.open
      },
      set(open) {
        this.open = open

        if (!this.isDesktop && !this.alwaysVisible) {
          const body = document.querySelector('body')

          if (open) {
            body.style.overflow = 'hidden'

            this.$nextTick(() => {
              if (this.$refs) {
                const { swiperWrapper } = this.$refs
                const monthHeihgt = this.$refs.datepickerMonth[0].offsetHeight
                const currentSelectionIndex = this.checkOut ? this.getMonthDiff(new Date(), this.checkOut) : 0

                swiperWrapper.scrollTop = currentSelectionIndex * monthHeihgt
              }
            })
          } else {
            body.style.overflow = ''
          }
        }

        this.$emit('input', this.open)
      },
    },
    sortBookings() {
      if (this.bookings.length > 0) {
        const bookings = [...this.bookings]

        return bookings.sort((a, b) => {
          const aa = a.checkInDate.split('/').reverse().join()
          const bb = b.checkOutDate.split('/').reverse().join()

          // eslint-disable-next-line no-nested-ternary
          return aa < bb ? -1 : aa > bb ? 1 : 0
        })
      }

      return []
    },
    duplicateBookingDates() {
      return this.baseHalfDayDates.filter(
        (
          (newArr) => (date) =>
            newArr.has(date) || !newArr.add(date)
        )(new Set()),
      )
    },
    baseHalfDayDates() {
      if (this.sortBookings.length > 0) {
        const bookings = this.sortBookings.map((x) => [x.checkInDate, x.checkOutDate])

        return bookings.reduce((a, b) => {
          return a.concat(b)
        })
      }

      return this.disabledDates
    },
    paginateMonths() {
      const months = [this.months[this.activeMonthIndex]]

      if (!(this.showSingleMonth || (this.alwaysVisible && !this.isDesktop))) {
        months.push(this.months[this.activeMonthIndex + 1])
      }

      return months
    },
    customTooltipMessage() {
      let tooltip = ''

      if (this.hoveringDate && (this.customTooltip || this.customTooltipHalfday)) {
        if (this.customTooltip && this.customTooltipHalfday) {
          tooltip = `${this.customTooltipHalfday}. <br/> ${this.customTooltip}`
        } else if (this.customTooltipHalfday && !this.customTooltip) {
          tooltip = this.customTooltipHalfday
        } else {
          tooltip = this.customTooltip
        }

        return tooltip
      }

      return this.tooltipMessage
    },
    sortedPeriodDates() {
      let periodDates = []

      if (this.periodDates) {
        const sortFunction = (fecha1, fecha2) => {
          const v1 = fecha1.startAt.split('/').reverse().join() + fecha1.endAt.split('/').reverse().join()
          const v2 = fecha2.startAt.split('/').reverse().join() + fecha2.endAt.split('/').reverse().join()

          // eslint-disable-next-line no-nested-ternary
          return v1 < v2 ? -1 : v1 > v2 ? 1 : 0
        }

        periodDates = [...this.periodDates].sort(sortFunction)
      }

      return periodDates
    },
    sliceMonthMobile() {
      const nbMonthRenderDom = 4

      if (this.activeMonthIndex >= nbMonthRenderDom) {
        return this.months.slice(this.activeMonthIndex - 3, this.activeMonthIndex + 1)
      }

      return this.months.slice(0, nbMonthRenderDom)
    },
    isPreventedMaxMonth() {
      const lastIndexMonthAvailable = this.getMonthDiff(this.startDate, this.lastDateAvailable)

      return this.activeMonthIndex >= lastIndexMonthAvailable - 1
    },
    isInCustomPeriod() {
      if (this.customPeriod.length) {
        return this.paginateMonths.some((month) =>
          this.customPeriod.some((p) => {
            return p === month.days[15].date.getMonth()
          }),
        )
      }

      return false
    },
    minNightCount() {
      return this.dynamicNightCounts || this.minNights
    },
    showClearSelectionButton() {
      return Boolean((this.checkIn || this.checkOut) && this.displayClearButton)
    },
    disabledWeekDaysObject() {
      const disabledDays = this.disabledDaysOfWeek.map((d) => d.toLowerCase())
      // const names = this.i18n['day-names']
      const names = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
      const SUNDAY = names[0]
      const MONDAY = names[1]
      const TUESDAY = names[2]
      const WEDNESDAY = names[3]
      const THURSDAY = names[4]
      const FRIDAY = names[5]
      const SATURDAY = names[6]
      // The order of _default is important!
      const disabledWeekDaysObject = {
        sunday: disabledDays.includes(SUNDAY),
        monday: disabledDays.includes(MONDAY),
        tuesday: disabledDays.includes(TUESDAY),
        wednesday: disabledDays.includes(WEDNESDAY),
        thursday: disabledDays.includes(THURSDAY),
        friday: disabledDays.includes(FRIDAY),
        saturday: disabledDays.includes(SATURDAY),
      }

      return Object.assign(disabledWeekDaysObject, this.disabledWeekDays)
    },
    disabledWeekDaysArray() {
      const days = this.disabledWeekDaysObject
      // const names = this.i18n['day-names']
      const names = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

      const fn = function fnDisabledWeekDaysArray(day, ix) {
        return day[1] ? names[ix] : false
      }

      return Object.entries(days)
        .map(fn)
        .filter((v) => v)
    },
    dayOptions() {
      return { ...this.$props, disabledWeekDaysObject: this.disabledWeekDaysObject }
    },
    numberOfMonths() {
      return this.showSingleMonth ? 1 : 2
    },
    isDesktop() {
      return this.screenSize === 'desktop'
    },
  },
  watch: {
    bookings() {
      this.createHalfDayDates(this.baseHalfDayDates)
      this.reRender()
    },
    checkIn(newDate) {
      this.$emit('check-in-changed', newDate)
      this.$emit('starting-date-changed', newDate)
      this.reRender()
    },
    checkOut(newDate) {
      this.$emit('ending-date-changed', newDate)

      if (this.checkOut !== null) {
        this.hoveringDate = null
        this.nextDisabledDate = null
        this.createHalfDayDates(this.baseHalfDayDates)
        this.reRender()
        this.showCustomTooltip = false
        this.isOpen = false
      }

      this.$emit('check-out-changed', newDate)
      this.reRender()
    },
    firstDayOfWeek(newDay) {
      this.$emit('first-day-of-week-changed', newDay)
      const startDate = new Date(this.startDate)
      const offset = this.numberOfMonths + this.activeMonthIndex

      this.generateInitialMonths()

      for (let i = this.numberOfMonths; i < offset; i++) {
        this.createMonth(new Date(startDate.getFullYear(), startDate.getMonth() + i, 1))
      }

      this.reRender()
    },
    startingDateValue(date) {
      this.setCheckIn(date)
    },
    endingDateValue(date) {
      this.setCheckOut(date)
    },
    singleDaySelection(single) {
      if (single) {
        this.setCheckOut(this.checkIn)
      } else {
        this.setCheckIn(this.checkIn)
        this.setCheckOut(null)
      }

      this.reRender()
    },
    yearBeforeMonth() {
      this.reRender()
    },
    i18n() {
      this.configureI18n()
    },
    disabledDates() {
      this.nextDisabledDate = null
      this.createHalfDayDates(this.baseHalfDayDates)
      this.reRender()
    },
  },
  created() {
    this.configureI18n()
    this.generateInitialMonths()
  },
  mounted() {
    this.handleWindowResize()

    window.addEventListener('resize', this.handleWindowResize)

    if (!this.isDesktop) {
      document.addEventListener('touchstart', this.handleTouchStart, false)
      document.addEventListener('touchmove', this.handleTouchMove, false)
      document.addEventListener('touchend', this.handleTouchEnd, false)
    } else {
      document.addEventListener('click', this.handleClickOutside, false)
      document.addEventListener('keyup', this.escFunction, false)
    }

    this.onElementHeightChange(document.body, () => {
      this.emitHeighChangeEvent()
    })
    this.createHalfDayDates(this.baseHalfDayDates)
  },
  destroyed() {
    window.removeEventListener('resize', this.handleWindowResize)

    if (!this.isDesktop) {
      document.removeEventListener('touchstart', this.handleTouchStart)
      document.removeEventListener('touchmove', this.handleTouchMove)
      document.removeEventListener('touchend', this.handleTouchEnd)
    } else {
      document.removeEventListener('keyup', this.escFunction, false)
      document.removeEventListener('click', this.handleClickOutside)
    }
  },
  methods: {
    ...Helpers,
    transformDisabledWeekDays() {},
    configureI18n() {
      fecha.setGlobalDateI18n({
        dayNames: this.i18n['day-names'],
        dayNamesShort: this.shortenString(this.i18n['day-names'], 3),
        monthNames: this.i18n['month-names'],
        monthNamesShort: this.shortenString(this.i18n['month-names'], 3),
        amPm: ['am', 'pm'],
        // D is the day of the month, function returns something like...  3rd or 11th
        DoFn(D) {
          return D + ['th', 'st', 'nd', 'rd'][D % 10 > 3 ? 0 : ((D - (D % 10) !== 10) * D) % 10]
        },
      })
    },
    generateInitialMonths() {
      this.months = []

      if (
        this.checkIn &&
        (this.getMonthDiff(this.getNextMonth(new Date(this.startDate)), this.checkIn) > 0 ||
          this.getMonthDiff(this.startDate, this.checkIn) > 0)
      ) {
        this.createMonth(new Date(this.startDate))
        const count = this.getMonthDiff(this.startDate, this.checkIn)
        const monthCount = this.showSingleMonth ? count - 1 : count
        let nextMonth = new Date(this.startDate)

        for (let i = 0; i <= monthCount; i++) {
          const tempNextMonth = this.getNextMonth(nextMonth)

          this.createMonth(tempNextMonth)
          nextMonth = tempNextMonth
        }

        if (this.checkOut && this.getMonthDiff(this.checkIn, this.checkOut) > 0) {
          this.createMonth(this.getNextMonth(nextMonth))
          this.activeMonthIndex = 1
        }

        this.activeMonthIndex += count
      } else {
        this.createMonth(new Date(this.startDate))

        if (!this.showSingleMonth) {
          this.createMonth(this.getNextMonth(new Date(this.startDate)))
        }
      }
    },
    handleBookingClicked(event, date, currentBooking) {
      this.$emit('booking-clicked', event, date, currentBooking)
      /**
       * @deprecated since v4.0.0 beta 11
       */
      this.$emit('bookingClicked', event, date, currentBooking)
    },
    escFunction(e) {
      const escTouch = 27

      if (e.keyCode === escTouch && this.isOpen && this.checkIn) {
        this.clearSelection()
      }
    },
    formatDate(date) {
      return this.dateFormater(date, this.format)
    },
    cleanString(string) {
      // eslint-disable-next-line no-useless-escape
      return string.replace(/\<br\/>/g, '')
    },
    dateIsInCheckInCheckOut(date) {
      const compareDate = this.dateFormater(date)
      let currentPeriod = null

      this.sortedPeriodDates.forEach((d) => {
        if (
          d.endAt !== compareDate &&
          (d.startAt === compareDate || this.validateDateBetweenTwoDates(d.startAt, d.endAt, compareDate))
        ) {
          currentPeriod = d
        }
      })

      return currentPeriod
    },
    dayIsDisabled(date) {
      if (
        this.checkIn &&
        !this.checkOut &&
        !this.isDateLessOrEquals(date, this.nextDisabledDate) &&
        this.nextDisabledDate !== Infinity
      ) {
        return true
      }

      if (this.checkIn && !this.checkOut && this.isDateLessOrEquals(date, this.checkIn)) {
        return true
      }

      return false
    },
    enterMonth(event, month) {
      this.$emit('enter-month', event, month)
    },
    enterDay(event, day) {
      const formatDate = this.dateFormater(day.date)
      const halfDays = Object.keys(this.checkIncheckOutHalfDay)
      const disableDays = this.disabledDates
        .filter((disableDate) => !halfDays.includes(disableDate))
        .includes(formatDate)

      if (!this.dayIsDisabled(day.date) && day.belongsToThisMonth && !disableDays) {
        this.setCustomTooltipOnHover(day)
      }

      this.hoveringDate = this.singleDaySelection ? null : day.date
      this.$emit('enter-day', event, day)
    },
    setCurrentPeriod(date, eventType) {
      let currentPeriod = {}

      if (this.sortedPeriodDates.length > 0) {
        this.sortedPeriodDates.forEach((d) => {
          if (
            eventType === 'click' &&
            (d.startAt === this.dateFormater(date) ||
              (d.endAt !== this.dateFormater(date) && this.validateDateBetweenTwoDates(d.startAt, d.endAt, date)))
          ) {
            currentPeriod = d
          } else if (
            eventType === 'hover' &&
            (d.startAt === this.dateFormater(date) || this.validateDateBetweenTwoDates(d.startAt, d.endAt, date))
          ) {
            currentPeriod = d
          }
        })

        if (Object.keys(currentPeriod).length > 0) {
          this.hoveringPeriod = currentPeriod
        } else if (this.minNightCount > 0 && this.checkIn) {
          this.hoveringPeriod = {
            periodType: 'nightly',
            minimumDuration: this.minNightCount,
            startAt: this.checkIn,
            endAt: this.addDays(this.checkIn, this.minNightCount),
          }
        } else {
          this.hoveringPeriod = {
            periodType: 'nightly',
            minimumDuration: this.minNightCount,
            startAt: this.checkIn,
            endAt: this.addDays(this.checkIn, this.minNightCount),
          }
        }
      } else if (this.minNightCount > 0) {
        this.hoveringPeriod = {
          periodType: 'nightly',
          minimumDuration: this.minNightCount,
          startAt: this.checkIn,
          endAt: this.addDays(this.checkIn, this.minNightCount),
        }
      }
    },
    setCustomTooltipOnHover(day) {
      const { date } = day

      this.hoveringDate = date
      if (this.showCustomTooltip) this.showCustomTooltip = false

      this.setCurrentPeriod(date, 'hover')

      if (Object.keys(this.hoveringPeriod).length > 0) {
        const { startNights = [], endNights = [] } = this.hoveringPeriod

        if (this.hoveringPeriod.startNight && !startNights.includes(this.hoveringPeriod.startNight)) {
          startNights.push(this.hoveringPeriod.startNight)
        }

        if (this.hoveringPeriod.endNight && !endNights.includes(this.hoveringPeriod.endNight)) {
          endNights.push(this.hoveringPeriod.endNight)
        }

        // Create tooltip
        if (this.hoveringPeriod.periodType === 'weekly_by_saturday') {
          const dayCodes = [6]
          const text = this.i18n.tooltip.saturdayToSaturday

          this.showTooltipWeeklyOnHover(date, dayCodes, text)
        } else if (this.hoveringPeriod.periodType === 'mon_fri_booking_only') {
          let dayCodes = [5]
          const text = this.i18n.tooltip.monToFridayOnly

          this.showTooltipWeeklyOnHover(date, dayCodes, text)

          dayCodes = [1]
          this.showTooltipWeeklyOnHover(date, dayCodes, text)
        } else if (this.hoveringPeriod.periodType === 'weekly_by_friday') {
          const dayCodes = [5]
          const text = this.i18n.tooltip.fridayToFriday

          this.showTooltipWeeklyOnHover(date, dayCodes, text)
        } else if (this.hoveringPeriod.periodType === 'nightly_by_friday') {
          const dayCodes = [5]
          const text = this.i18n.tooltip.fridayToMonday

          this.showTooltipWeeklyOnHover(date, dayCodes, text)
        } else if (this.hoveringPeriod.periodType === 'nightly_by_monday') {
          const dayCodes = [1]
          const text = this.i18n.tooltip.monToFridayOnly

          this.showTooltipWeeklyOnHover(date, dayCodes, text)
        } else if (this.hoveringPeriod.periodType === 'weekly_by_sunday') {
          const dayCodes = [0]
          const text = this.i18n.tooltip.sundayToSunday

          this.showTooltipWeeklyOnHover(date, dayCodes, text)
        } else if (this.hoveringPeriod.periodType === 'nightly' && startNights.length) {
          const dayCodes = startNights
          const { customTooltip } = this.hoveringPeriod
          let text = ''

          if (customTooltip) {
            text = this.i18n.tooltip[customTooltip]
          } else if (dayCodes.length === 1 && dayCodes[0] === 1) {
            text = this.i18n.tooltip.monToFridayOnly
          } else if (dayCodes.length === 1 && dayCodes[0] === 5) {
            text = this.i18n.tooltip.fridayToMonday
          }

          // startNight / endNight type activate tooltip
          this.showTooltipWeeklyOnHover(date, dayCodes, text, endNights)
        } else if (this.hoveringPeriod.periodType === 'nightly') {
          this.showTooltipNightlyOnHover(date)
        } else {
          // Clean tooltip
          this.showCustomTooltip = false
          this.customTooltip = ''
        }
      } else {
        this.hoveringPeriod = {}
      }

      if (this.halfDay) {
        this.createHalfDayTooltip(day.date)
      }
    },
    handleDayClick(event, date, formatDate, resetCheckin) {
      this.nextPeriodDisableDates = []

      if (resetCheckin) {
        this.clearSelection()
        this.$nextTick(() => {
          this.handleDayClick(event, date, formatDate, false)
        })

        return
      }

      let nextDisabledDate =
        (this.maxNights ? this.addDays(date, this.maxNights + 1) : null) ||
        this.getNextDate(this.sortedDisabledDates, date) ||
        this.nextDateByDayOfWeekArray(this.disabledWeekDaysArray, date, this.i18n) ||
        this.nextBookingDate(date) ||
        Infinity

      this.dynamicNightCounts = null

      if (this.enableCheckout) {
        nextDisabledDate = Infinity
      }

      if (this.checkIn == null && !this.singleDaySelection) {
        this.checkIn = date
        this.$emit('check-in-selected', date)
        this.setMinimumDuration(date)
      } else if (this.singleDaySelection) {
        this.checkIn = date
        this.$emit('check-in-selected', date)
        this.checkOut = date
      } else if (this.checkIn !== null && this.checkOut == null && this.isDateLessOrEquals(date, this.checkIn)) {
        this.checkIn = date
        this.$emit('check-in-selected', date)
      } else if (this.checkIn !== null && this.checkOut == null) {
        this.checkOut = date
        this.$emit('period-selected', event, this.checkIn, this.checkOut)
        /**
         * @deprecated since v4.0.0 beta 11
         */
        this.$emit('periodSelected', event, this.checkIn, this.checkOut)
      } else {
        this.checkOut = null
        this.checkIn = date
        this.$emit('check-in-selected', date)
        this.setMinimumDuration(date)
      }

      if (this.checkIn && !this.checkOut) {
        this.setCurrentPeriod(date, 'click')
        this.checkInPeriod = this.hoveringPeriod
        this.setCustomTooltipOnClick()
      }

      this.nextDisabledDate = nextDisabledDate
      this.hoveringDate = null
      this.hoveringDate = date
      this.$emit('day-clicked', date, formatDate, nextDisabledDate)
      /**
       * @deprecated since v4.0.0 beta 11
       */
      this.$emit('dayClicked', date, formatDate, nextDisabledDate)
    },
    nextBookingDate(date) {
      let closest = Infinity

      if (this.sortBookings.length > 0) {
        const nextDateFormated = this.dateFormater(this.addDays(date, 1))
        const nextBooking = this.sortBookings.find(
          (booking) =>
            this.validateDateBetweenDate(booking.checkInDate, nextDateFormated) ||
            this.validateDateBetweenTwoDates(booking.checkInDate, booking.checkOutDate, nextDateFormated),
        )

        closest = nextBooking ? nextBooking.checkInDate : Infinity
      }

      return closest
    },
    setCustomTooltipOnClick() {
      if (Object.keys(this.checkInPeriod).length > 0 && this.checkInPeriod.periodType.includes('weekly')) {
        const nextValidDate = this.addDays(this.checkIn, this.minNightCount)

        this.checkInPeriod.nextValidDate = nextValidDate
        this.showTooltipWeeklyOnClick()
      } else if (this.checkInPeriod.periodType === 'nightly') {
        this.showTooltipNightlyOnClick()
      }
    },
    showTooltipWeeklyOnHover(date, periodDayType, text, endNights = []) {
      const countDaysBetweenCheckInCurrentDay = this.countDays(this.checkIn, date)
      let notOnPeriodDayType = !periodDayType.includes(date.getDay())

      // this code updates the tooltip on startNight / endNight type nightly options
      if (endNights.length && this.checkIn) {
        notOnPeriodDayType = !endNights.includes(date.getDay())
      }

      const isCheckInCheckOut = this.checkIn && this.checkOut
      const notCheckInNotPeriodDayType = !this.checkIn && notOnPeriodDayType
      const isCheckInNotCheckOut = this.checkIn && !this.checkOut
      const isNotBetweenCheckInAndCheckOut = !this.validateDateBetweenTwoDates(this.checkIn, this.checkOut, date)
      const notAllowDaysBetweenCheckInAndNextValidDate =
        this.hoveringPeriod.nextValidDate &&
        this.validateDateBetweenTwoDates(this.checkIn, this.hoveringPeriod.nextValidDate, this.hoveringDate) &&
        this.dateFormater(this.checkIn) !== this.dateFormater(this.hoveringDate) &&
        this.dateFormater(this.hoveringPeriod.nextValidDate) !== this.dateFormater(this.hoveringDate)
      const hasHalfDayOnWeeklyPeriod =
        Object.keys(this.checkIncheckOutHalfDay).length > 0 &&
        this.checkIncheckOutHalfDay[this.dateFormater(date)] &&
        this.checkIncheckOutHalfDay[this.dateFormater(date)].checkIn

      // Show tooltip on not-allowed day
      if (notCheckInNotPeriodDayType) {
        this.showCustomTooltip = true
        this.customTooltip = text
      } else {
        this.showCustomTooltip = false
        this.customTooltip = ''
      }

      // Show tooltip when CheckIn
      if (isCheckInNotCheckOut) {
        const nextDayValid = this.addDays(this.checkIn, this.minNightCount)
        const isDateAfterMinimumDuration = this.getDayDiff(date, nextDayValid) <= 0

        if (isDateAfterMinimumDuration && notOnPeriodDayType) {
          this.showCustomTooltip = true
          this.customTooltip = text
        } else if (notOnPeriodDayType || notAllowDaysBetweenCheckInAndNextValidDate) {
          if (this.checkInPeriod && this.checkInPeriod.periodType === 'nightly') {
            this.showCustomTooltip = false
            this.customTooltip = ''
          } else {
            // Show default message on currentDay
            const night = this.pluralize(this.minNightCount, 'week')

            this.showCustomTooltip = true
            this.customTooltip = this.completeTrad(this.i18n.tooltip.minimumRequiredPeriod, {
              minNightInPeriod: this.minNightCount / 7,
              night,
            })
          }
        } else if (hasHalfDayOnWeeklyPeriod) {
          // Show the correct wording in comparison to periodType of this.checkInPeriod equal to "nightly" / "weekly"
          if (this.checkInPeriod.periodType !== 'nightly') {
            this.customTooltip = `${countDaysBetweenCheckInCurrentDay / 7} ${this.pluralize(
              this.minNightCount,
              'week',
            )}`
          } else if (this.checkInPeriod.periodType === 'nightly') {
            this.customTooltip = `${countDaysBetweenCheckInCurrentDay} ${
              countDaysBetweenCheckInCurrentDay !== 1 ? this.i18n.nights : this.i18n.night
            }`
          }
        } else {
          // Clean tooltip
          this.showCustomTooltip = false
          this.customTooltip = ''
        }
        // Show tooltip when CheckIn & CheckOut on all the days that are not between checkIn and CheckOut
      } else if (isCheckInCheckOut && notOnPeriodDayType && isNotBetweenCheckInAndCheckOut) {
        this.showCustomTooltip = true
        this.customTooltip = text
      }
    },
    showTooltipWeeklyOnClick() {
      const night = this.pluralize(this.minNightCount, 'week')

      this.showCustomTooltip = true
      this.customTooltip = this.completeTrad(this.i18n.tooltip.minimumRequiredPeriod, {
        minNightInPeriod: this.minNightCount / 7,
        night,
      })
    },
    showTooltipNightlyOnHover(date) {
      if (this.checkIn && !this.checkOut) {
        const nextDayValid = this.addDays(this.checkIn, this.minNightCount)
        const isDateAfterMinimumDuration = this.getDayDiff(date, nextDayValid) <= 0
        const countOfDays = this.countDays(this.checkIn, date)
        const night = this.pluralize(Math.max(this.minNightCount, countOfDays))

        if (!isDateAfterMinimumDuration && (this.showTooltipOnOneDay || countOfDays > 1)) {
          const minNightInPeriod = this.hoveringPeriod.minimumDuration

          this.showCustomTooltip = true
          this.customTooltip = this.completeTrad(this.i18n.tooltip.minimumRequiredPeriod, {
            minNightInPeriod,
            night,
          })
        } else {
          this.customTooltip = `${countOfDays} ${night}`
        }
      } else {
        this.customTooltip = ''
      }
    },
    showTooltipNightlyOnClick() {
      const minNightInPeriod = this.hoveringPeriod.minimumDuration
      const night = this.pluralize(this.minNightCount)

      this.showCustomTooltip = true
      this.customTooltip = this.completeTrad(this.i18n.tooltip.minimumRequiredPeriod, { minNightInPeriod, night })
    },
    createHalfDayTooltip(date) {
      this.customTooltipHalfday = ''
      const formatedHoveringDate = this.dateFormater(date)

      if (this.checkIncheckOutHalfDay[formatedHoveringDate]) {
        this.showCustomTooltip = true

        if (this.checkIncheckOutHalfDay[formatedHoveringDate].checkIn) {
          this.customTooltipHalfday = this.i18n.tooltip.halfDayCheckOut
        } else if (this.checkIncheckOutHalfDay[formatedHoveringDate].checkOut) {
          this.customTooltipHalfday = this.i18n.tooltip.halfDayCheckIn
        }
      }
    },
    completeTrad(translation, keys) {
      let newT = translation
      const keysTranslations = Object.keys(keys)

      keysTranslations.forEach((key) => {
        newT = newT.replace(`%{${key}}`, keys[key])
      })

      return newT
    },
    handleClickOutside(event) {
      const ignoreClickOnMeElement = this.$refs[`DatePicker-${this.hash}`]

      if (ignoreClickOnMeElement) {
        const isClickInsideElement = ignoreClickOnMeElement.contains(event.target)

        if (!isClickInsideElement) {
          this.hideDatepicker()
        }
      }
    },
    handleWindowResize() {
      if (window.innerWidth < 480) {
        this.screenSize = 'smartphone'
      } else if (window.innerWidth >= 480 && window.innerWidth < 768) {
        this.screenSize = 'tablet'
      } else if (window.innerWidth >= 768) {
        this.screenSize = 'desktop'
      }

      return this.screenSize
    },
    onElementHeightChange(el, callback) {
      let lastHeight = el.clientHeight
      let newHeight = lastHeight
      const newEl = el

      ;(function run() {
        newHeight = el.clientHeight

        if (lastHeight !== newHeight) {
          callback()
        }

        lastHeight = newHeight

        if (newEl.onElementHeightChangeTimer) {
          clearTimeout(el.onElementHeightChangeTimer)
        }

        newEl.onElementHeightChangeTimer = setTimeout(run, 1000)
      })()
    },
    emitHeighChangeEvent() {
      this.$emit('height-changed')
    },
    reRender() {
      this.datepickerDayKey += 1
      this.datepickerMonthKey += 1
      this.datepickerWeekKey += 1
    },
    clearSelection() {
      this.hoveringDate = null
      this.checkIn = null
      this.checkOut = null
      this.nextDisabledDate = null
      this.nextPeriodDisableDates = []
      this.showCustomTooltip = false
      this.hoveringPeriod = {}
      this.checkInPeriod = {}
      this.createHalfDayDates(this.baseHalfDayDates)
      this.reRender()
      this.$emit('clear-selection')
    },
    closeMobileDatepicker() {
      this.hideDatepicker()
    },
    hideDatepicker() {
      this.isOpen = false
    },
    showDatepicker() {
      this.isOpen = true
    },
    toggleDatepicker() {
      this[this.isOpen ? 'hideDatepicker' : 'showDatepicker']()
    },
    clearCheckIn() {
      if (this.checkIn && !this.checkOut) {
        this.clearSelection()
      }
    },
    clickOutside() {
      if (this.closeDatepickerOnClickOutside) {
        this.hideDatepicker()
      }
    },
    setMinimumDuration(date) {
      if (this.sortedPeriodDates) {
        let nextPeriod = null
        let currentPeriod = null
        const compareDate = this.dateFormater(date)

        this.sortedPeriodDates.forEach((d) => {
          if (
            d.endAt !== compareDate &&
            (d.startAt === compareDate || this.validateDateBetweenTwoDates(d.startAt, d.endAt, date))
          ) {
            currentPeriod = d
          }
        })

        if (currentPeriod) {
          this.sortedPeriodDates.forEach((period) => {
            if (period.startAt === currentPeriod.endAt) {
              nextPeriod = period
            }
          })

          if (this.checkIn && !this.checkOut && nextPeriod) {
            const endNextPeriod = this.addDays(nextPeriod.startAt, nextPeriod.minimumDuration - 1)
            const startNextPeriodPlusOne = this.addDays(nextPeriod.startAt, 1)
            const newDisablesDates = this.getDaysArray(startNextPeriodPlusOne, endNextPeriod)

            this.nextPeriodDisableDates = newDisablesDates
          }

          if (currentPeriod.periodType === 'nightly' && currentPeriod.endAt !== date) {
            this.dynamicNightCounts = currentPeriod.minimumDuration
          }

          if (
            currentPeriod.periodType === 'weekly_by_saturday' ||
            currentPeriod.periodType === 'weekly_by_sunday' ||
            currentPeriod.periodType === 'weekly_by_friday'
          ) {
            const minimumDuration = currentPeriod.minimumDuration * 7

            this.dynamicNightCounts = minimumDuration
          }

          if (currentPeriod.periodType === 'mon_fri_booking_only') {
            // const minimumDuration = currentPeriod.minimumDuration * 7
            this.dynamicNightCounts = currentPeriod.minimumDuration
          }
        } else {
          this.dynamicNightCounts = 0
        }
      }
    },
    renderPreviousMonth() {
      if (this.activeMonthIndex >= 1) {
        const firstDayOfLastMonth = this.months[this.activeMonthIndex].days.filter(
          (day) => day.belongsToThisMonth === true,
        )
        const previousMonth = this.getPreviousMonth(firstDayOfLastMonth[0].date)

        this.activeMonthIndex--

        this.datepickerDayKey++
        this.datepickerMonthKey++
        this.$emit('previous-month-rendered', previousMonth)
      }
    },
    renderNextMonth: throttle(function throttleRenderNextMonth() {
      if (
        (!this.showSingleMonth && this.activeMonthIndex < this.months.length - 2) ||
        (this.showSingleMonth && this.activeMonthIndex < this.months.length - 1)
      ) {
        this.activeMonthIndex++

        return
      }

      let firstDayOfLastMonth

      if (!this.isDesktop || this.showSingleMonth) {
        firstDayOfLastMonth = this.months[this.months.length - 1].days.filter((day) => day.belongsToThisMonth === true)
      } else {
        firstDayOfLastMonth = this.months[this.activeMonthIndex + 1].days.filter(
          (day) => day.belongsToThisMonth === true,
        )
      }

      if (this.endDate !== Infinity) {
        if (fecha.format(firstDayOfLastMonth[0].date, 'YYYYMM') === fecha.format(new Date(this.endDate), 'YYYYMM')) {
          return
        }
      }

      const nextMonth = this.getNextMonth(firstDayOfLastMonth[0].date)

      this.createMonth(nextMonth)
      this.activeMonthIndex++
      this.$emit('next-month-rendered', nextMonth)
      this.datepickerDayKey++
      this.datepickerMonthKey++
    }, 350),
    setCheckIn(date) {
      this.checkIn = date
    },
    setCheckOut(date) {
      this.checkOut = date
    },
    createMonth(date) {
      const firstDay = this.getFirstDay(date, this.firstDayOfWeek)
      const month = {
        days: [],
      }

      for (let i = 0; i < 42; i++) {
        month.days.push({
          date: this.addDays(firstDay, i),
          belongsToThisMonth: this.addDays(firstDay, i).getMonth() === date.getMonth(),
        })
      }

      this.months.push(month)
    },
    createHalfDayDates(_baseHalfDayDates) {
      let sortedDates = []
      const checkIncheckOutHalfDay = {}
      const baseHalfDayDates = [..._baseHalfDayDates]

      // Sorted disabledDates
      baseHalfDayDates.sort((a, b) => {
        const aa = a.split('/').reverse().join()
        const bb = b.split('/').reverse().join()

        // eslint-disable-next-line no-nested-ternary
        return aa < bb ? -1 : aa > bb ? 1 : 0
      })

      if (this.sortBookings.length === 0) {
        for (let i = 0; i < baseHalfDayDates.length; i++) {
          const newDate = baseHalfDayDates[i]

          if (this.halfDay) {
            const newDateIncrementOne = baseHalfDayDates[i + 1]

            if (i === 0) {
              checkIncheckOutHalfDay[newDate] = {
                checkIn: true,
              }
            }

            if (
              !checkIncheckOutHalfDay[newDate] &&
              baseHalfDayDates[i + 1] &&
              this.getDayDiff(newDate, newDateIncrementOne) > 1
            ) {
              checkIncheckOutHalfDay[newDate] = {
                checkOut: true,
              }
              checkIncheckOutHalfDay[newDateIncrementOne] = {
                checkIn: true,
              }
            }

            if (i === baseHalfDayDates.length - 1) {
              checkIncheckOutHalfDay[baseHalfDayDates[baseHalfDayDates.length - 1]] = {
                checkOut: true,
              }
            }
          }

          sortedDates[i] = baseHalfDayDates[i]
        }
      } else {
        this.sortBookings.forEach((booking) => {
          checkIncheckOutHalfDay[booking.checkInDate] = {
            checkIn: true,
          }
          checkIncheckOutHalfDay[booking.checkOutDate] = {
            checkOut: true,
          }
        })
      }

      if (this.halfDay) {
        const halfDays = Object.keys(checkIncheckOutHalfDay)

        sortedDates = sortedDates.filter((date) => !halfDays.includes(date))
      }

      sortedDates = sortedDates.map((date) => new Date(date))
      this.sortedDisabledDates = sortedDates.sort((a, b) => a - b)
      this.checkIncheckOutHalfDay = checkIncheckOutHalfDay
      this.$emit('handle-checkin-checkout-half-day', this.checkIncheckOutHalfDay)
      /**
       * @deprecated since v4.0.0 beta 11
       */
      this.$emit('handleCheckinCheckoutHalfDay', this.checkIncheckOutHalfDay)
    },
  },
}
</script>
