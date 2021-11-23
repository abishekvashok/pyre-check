(*
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *)

open Ast

module Unit : sig
  type t [@@deriving eq, show]

  val empty : t

  val top : t

  val create : Annotation.t -> t

  val create_mutable : Type.t -> t

  val base : t -> Annotation.t option

  val set_base : t -> base:Annotation.t -> t

  val set_annotation
    :  ?wipe_subtree:bool ->
    attribute_path:Reference.t ->
    annotation:Annotation.t ->
    t ->
    t

  val get_annotation : attribute_path:Reference.t -> t -> Annotation.t option

  val less_or_equal : global_resolution:GlobalResolution.t -> left:t -> right:t -> bool

  val join : global_resolution:GlobalResolution.t -> t -> t -> t

  val meet : global_resolution:GlobalResolution.t -> t -> t -> t

  val widen
    :  global_resolution:GlobalResolution.t ->
    widening_threshold:int ->
    previous:t ->
    next:t ->
    iteration:int ->
    t
end

module Store : sig
  type t = {
    annotations: Unit.t Reference.Map.t;
    temporary_annotations: Unit.t Reference.Map.t;
  }
  [@@deriving eq, show]

  val empty : t

  val get_base : name:Reference.t -> t -> Annotation.t option

  val get_annotation : name:Reference.t -> attribute_path:Reference.t -> t -> Annotation.t option

  val set_base : ?temporary:bool -> name:Reference.t -> base:Annotation.t -> t -> t

  val new_as_base : ?temporary:bool -> name:Reference.t -> base:Annotation.t -> t -> t

  val set_annotation
    :  ?temporary:bool ->
    ?wipe_subtree:bool ->
    name:Reference.t ->
    attribute_path:Reference.t ->
    base:Annotation.t option ->
    annotation:Annotation.t ->
    t ->
    t

  val less_or_equal : global_resolution:GlobalResolution.t -> left:t -> right:t -> bool

  val less_or_equal_monotone : left:t -> right:t -> bool
end